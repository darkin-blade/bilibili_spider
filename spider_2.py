# 爆搜所有(包括下架)的番剧

import json
import requests

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
    def get_results(self, filename):
        # 筛选爆搜结果
        results = {}
        season_list = []
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
                season_list.append(view)
        results.update({"season": season_list})
        with open(filename, 'w') as f:
            f.write(json.dumps(results, indent = 2, ensure_ascii = False))

if __name__ == '__main__':
    my_spider = Spider_season()
    my_spider.get_results("force.json")
