# 说明

番剧索引

# 示例

https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=50&type=1

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

- `st`
未知,默认为1

- `sort`
| value | 含义 |
| :--: | :--: |
| 0 | 降序 |
| 1 | 升序 |

- `page`

- `season_type`
未知,默认为1

- `pagesize`

`type`
未知,默认为1
