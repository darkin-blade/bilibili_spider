# 爆搜所有(包括下架)的番剧,并存入mysql

import json
import pymysql
import requests
import time

class Spider_season:
    cursor = None
    db = None

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

    def send_request(self, season_id):
        # 获取aid
        url = 'https://api.bilibili.com/pgc/web/season/section?season_id={}'
        result = requests.get(url.format(season_id))
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

    def get_detail(self, season_id):
        # 获取详细信息
        result = self.send_request(season_id) # 爆搜season
        if result['code'] == 0: # 获取成功
            # if 'main_section' not in result['result']:
                # TODO 异常情况
            aid = result['result']['main_section']['episodes'][0]['aid'] 
            # TODO 获取aid
            item = {
                    "season_id": season_id,
                    "aid": aid,
                    "title": "没有标题",
                    }
            view = self.get_view(aid) # 刷新aid, title
            item.update(view)
            print(item)
            self.insert_sql(item)

    def insert_sql(self, item):
        if self.db == None:
            print("no database")
            return
        cmd = 'insert into season (season_id, aid, title, p_year, p_month, p_day, c_year, c_month, c_day) values' + \
                '({}, {}, \'{}\', {}, {}, {}, {}, {}, {});'
        cmd = cmd.format(
            item['season_id'], 
            item['aid'],
            item['title'],
            item['p_year'],
            item['p_month'],
            item['p_day'],
            item['c_year'],
            item['c_month'],
            item['c_day']
            )
        self.cursor.execute(cmd)

if __name__ == '__main__':
    my_spider = Spider_season()
    my_spider.init_sql()

    for i in range(1, 10):
        my_spider.get_detail(i)
        if i % 5 == 0:
            # 刷新数据库
            my_spider.db.commit()

    my_spider.db.commit()
    my_spider.db.close()
