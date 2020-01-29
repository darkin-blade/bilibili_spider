# api记录

## [https://bangumi.bilibili.com/media/web_api/search/result?page=101&season_type=1&pagesize=20000](https://bangumi.bilibili.com/media/web_api/search/result?page=101&season_type=1&pagesize=20000)
(旧版?)番剧->番剧索引

## [https://bangumi.bilibili.com/web_api/timeline_global](https://bangumi.bilibili.com/web_api/timeline_global)
未知api

## [https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1](https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1)

番剧->番剧索引

- `season_version`类型
| value | 含义 |
| :--: | :--: |
| -1 | 所有类型 |
| 1 | 正片 |
| 2 | 电影 |
| 3 | 其他(ova,sp等) |

- `area`地区

- `is_finish`状态

- `copyright`版权

- `season_status`付费

- `season_month`季度

- `year`时间

- `style_id`风格
- `order`
| value | 含义 |
| :--: | :--: |
| 0 | 更新时间 |
| 1 | 未知 |
| 2 | 播放数量 |
| 3 | 追番人数 |
| 4 | 最高评分 |
| 5 | 开播时间 |
https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1
