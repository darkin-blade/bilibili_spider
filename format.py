def bangumi():
    url = 'https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order={}&st=1&sort={}&page={}&season_type=1&pagesize=50&type=1'
    print(url.format("5", "1", "50"))

if __name__ == '__main__':
    bangumi()
