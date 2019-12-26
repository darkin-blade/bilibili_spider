import requests
# 吃屎
class BilibiliVideo:
  def __init__(self, season_id, media_id, title):
    self.season_id = season_id
    self.media_id = media_id
    self.title = title

request_url = 'https://bangumi.bilibili.com/media/web_api/search/result?page={}&season_type=1&pagesize=20'
page = 1

tmp_url = request_url.format(page);