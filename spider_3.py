# 爆搜所有(包括下架)的番剧,并存入mysql

import json
import pymysql
import requests
import threading
import time

class Spider_season:
    cursor = None
    db = None
    threads = [] # 线程list
    results = [] # 所有结果
    failed = [] # 失败的season_id
    empty = [] # 无效的season_id
    log = [] # 确保没有遗漏

    def send_request(self, season_id):
        # 获取aid
        url = 'https://api.bilibili.com/pgc/web/season/section?season_id={}'
        result = requests.get(url.format(season_id))
        # print(result)
        # TODO 被封杀
        return json.loads(result.text)

    def get_view(self, aid):
        # 获取番剧名
        url = 'https://api.bilibili.com/x/web-interface/view?aid={}'
        result = requests.get(url.format(aid))
        view = json.loads(result.text)
        item = {
                "title": "NULL",
                "p_year": 0,
                "p_month": 0,
                "p_day": 0,
                "c_year": 0,
                "c_month": 0,
                "c_day": 0
                }
        if 'data' not in view:
            # 异常情况
            item['title'] = "仅限港澳台"
        else:
            pubdate = time.localtime(view['data']['pubdate'])
            ctime = time.localtime(view['data']['ctime'])
            item.update({
                "title": view['data']['title'],
                "p_year": pubdate.tm_year,
                "p_month": pubdate.tm_mon,
                "p_day": pubdate.tm_mday,
                "c_year": ctime.tm_year,
                "c_month": ctime.tm_mon,
                "c_day": ctime.tm_mday
                })
        return item

    def get_detail(self, season_id, num = 1, upper = 100000):
        # 获取详细信息
        group = [] # 按组存放结果
        for i in range(num):
            if (season_id + i >= upper):
                # 超出上界
                break
            result = self.send_request(season_id + i) # 爆搜season
            # 添加记录
            self.log.append(season_id + i)
            if result['code'] == 0: # 获取成功
                aid = 0
                ep_id = 0 # id 是关键字
                if 'main_section' in result['result']:
                    aid = result['result']['main_section']['episodes'][0]['aid'] 
                    ep_id = result['result']['main_section']['episodes'][0]['id']
                else:
                    # TODO 没有版权
                    # TODO 只有预告,暂未上映
                    self.failed.append({
                        "season_id": season_id + i,
                        "aid": aid,
                        "id": ep_id
                        })
                    continue
                item = {
                        "season_id": season_id + i,
                        "aid": aid,
                        "id": ep_id,
                        "title": "没有标题",
                        }
                view = self.get_view(aid) # 刷新aid, title
                item.update(view)
                # print(item)
                group.append(item)
            else:
                self.empty.append({"season_id": season_id})
            if result['code'] == 0:
                print('\033[1;32m%d\033[0m' % (season_id + i))
            else:
                if (i % 20 == 0):
                    print('\033[34m%d\033[0m' % (season_id + i))
        self.results.extend(group)

    def init_sql(self):
        self.db = pymysql.connect(
                host = 'localhost',
                port = 3306, # 端口错误错误代码111
                user = 'niabie',
                passwd = None,
                db = 'bilibili',
                charset = 'utf8'
                )
        self.cursor = self.db.cursor()

    def insert_season(self, item):
        if self.db == None:
            print("no database")
            return
        cmd = 'insert ignore into season (season_id, aid, id, title, p_year, p_month, p_day, c_year, c_month, c_day) values' + \
                '({}, {}, {}, \'{}\', {}, {}, {}, {}, {}, {});'
        cmd = cmd.format(
            item['season_id'], 
            item['aid'],
            item['id'],
            item['title'].replace("'", "''").replace("\\", ""),
            item['p_year'],
            item['p_month'],
            item['p_day'],
            item['c_year'],
            item['c_month'],
            item['c_day']
            )
        self.cursor.execute(cmd)

    def insert_failed(self, item):
        # 记录获取失败的记录
        if self.db == None:
            print("no database")
            return
        cmd = 'insert ignore into failed (season_id, aid, id) values' + \
                '({}, {}, {});'
        cmd = cmd.format(
            item['season_id'],
            item['aid'],
            item['id']
            )
        self.cursor.execute(cmd)

    def start_request(self, low, high):
        # 抓取 [low, high) 的数据
        group_size = 200
        thread_num = 5

        total = high - low
        if total > (group_size * thread_num):
            # 使用多次循环
            loop = int(total / (group_size * thread_num) + 1)
            for j in range(loop):
                print('loop', j)
                for i in range(0, 5):
                    # TODO 限定上界
                    t = threading.Thread(
                            target = my_spider.get_detail,
                            args = (low + i * group_size + j * group_size * thread_num, group_size, high)) # TODO 基数
                    t.start()
                    self.threads.append(t) # 加入线程list
                for t in self.threads:
                    t.join()
                    print(t, 'finished')
                self.threads.clear() # 清空所有线程
                self.start_commit()
        elif total > group_size:
            # 使用多线程
            for i in range(0, 5):
                # TODO 限定上界
                t = threading.Thread(
                        target = my_spider.get_detail,
                        args = (low + i * group_size, group_size, high))
                t.start()
                self.threads.append(t) # 加入线程list
            for t in self.threads:
                t.join()
                print(t, 'finished')
            self.threads.clear() # 清空所有线程
            self.start_commit()
        elif total > 0:
            # 使用单线程
            self.get_detail(low, total)
            self.start_commit()
        # 输出所有遗漏的season
        for i in range(low, high):
            if i not in self.log:
                print('\033[1;31m%d\033[0m' % (i))

    def start_commit(self):
        print('start commit')
        for item in self.results:
            self.insert_season(item)
        for f in self.failed: # 记录保存失败的数据
            self.insert_failed(f)
        self.db.commit()
        # 清空数据
        self.results.clear()
        self.failed.clear()
        print('commit finish')


if __name__ == '__main__':
    my_spider = Spider_season()
    my_spider.init_sql()

    my_spider.start_request(24000, 30000)

    my_spider.db.close()
