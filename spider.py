import requests
import json

class Spider:
    url = 'https://api.bilibili.com/pgc/season/index/result?' + \
    'season_version=-1&' + \
    'area=-1&is_finish=-1&' + \
    'copyright=-1&' + \
    'season_status=-1&' + \
    'season_month=-1&' + \
    'year=-1&' + \
    'style_id=-1&' + \
    'order={}&' +  \
    'st=1&' + \
    'sort={}&' + \
    'page={}&' + \
    'season_type=1&' + \
    'pagesize=50&' + \
    'type=1'
    results = {}
    # order
    # 0: 追番, 1: 未知, 2: 播放数量, 3: 追番人数, 4: 最高评分, 5: 开播时间
    # sort
    # 0: 降序, 1: 升序
    def format_request(self):
        order = 5
        sort = 1
        page = 61
        print(self.url.format(order, sort, page))
    def start_request(self):
        order = 5
        sort = 1
        for page in range(1, 100):
            result = requests.get(self.url.format(order, sort, page))
            yield result
    def get_result(self):
        for result in self.start_request():
            res_list = json.loads(result.text)
            if ('list' not in res_list['data']):
                print('end')
                break
            for res_item in res_list['data']['list']:
                # print(res_item['title'], res_item['order'])
                # 合并所有结果
                self.results.update({res_item['title']: res_item['order']})
    def save_result(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.results, indent = 2, ensure_ascii = False))

if __name__ == '__main__':
    my_spider = Spider()
    my_spider.get_result()
    my_spider.save_result("tmp.json")
