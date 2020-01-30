# 爆搜所有(包括下架)的番剧,并存入mysql

import json
import pymysql
import requests
import time

class Spider_season:
    def send_requests(self):
        # 暴力发送request
        url = 'https://api.bilibili.com/pgc/web/season/section?season_id={}'
        for i in range(0, 5000):
            result = requests.get(url.format(i))
            yield [i, json.loads(result.text)]
    def get_view(self, aid):
        # 获取番剧名
        url = 'https://api.bilibili.com/x/web-interface/view?aid={}'
        result = requests.get(url.format(aid))
        res_json = json.loads(result.text)
        title = "NULL"
        if 'data' not in res_json:
            # 异常情况
            title = "仅限港澳台"
        else:
            title = res_json['data']['title']
        return {"aid": aid,
                "title": title}
    def get_results(self):
        # 筛选爆搜结果
        for result in self.send_requests():
            season_id = result[0]
            response = result[1] # json
            if response['code'] == 0: # 获取成功
                if 'main_section' not in response['result']:
                    # 异常情况
                    view = {"season_id": season_id}
                else:
                    aid = response['result']['main_section']['episodes'][0]['aid']
                    # TODO 获取aid
                    view = self.get_view(aid)
                    view.update({"season_id": season_id})
                print(view)

if __name__ == '__main__':
    db = pymysql.connect(
            host = 'localhost',
            port = 3306, # 端口错误错误代码111
            user = 'niabie',
            passwd = None,
            db = 'bilibili',
            charset = 'utf8'
            )
    cursor = db.cursor()
    test = {
            "season_id": 0,
            "aid": 0,
            "title": "爱上对方就卡死了地方就是打卡了",
            "p_year": 0,
            "p_month": 0,
            "p_day": 0,
            "c_year": 0,
            "c_month": 0,
            "c_day": 0
            }
    cmd = 'insert into season (season_id, aid, title, p_year, p_month, p_day, c_year, c_month, c_day) values' + \
            '({}, {}, \'{}\', {}, {}, {}, {}, {}, {});'
    cmd = cmd.format(
            test['season_id'], 
            test['aid'],
            test['title'],
            test['p_year'],
            test['p_month'],
            test['p_day'],
            test['c_year'],
            test['c_month'],
            test['c_day']
            )
    cursor.execute(cmd)
    db.commit()
    db.close()
