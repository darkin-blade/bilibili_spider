# 说明

番剧分集

# 示例

`https://api.bilibili.com/pgc/web/season/section?season_id=29590`(Re:0新编集版)

```json
{
    "code": 0,
    "message": "success",
    "result": {
        "main_section": {
            "episodes": [{
                "aid": 81626494,
                "badge": "",
                "badge_type": 0,
                "cid": 139676062,
                "cover": "http://i0.hdslb.com/bfs/archive/371c2a7771b3e76ff2e4a75c72332ff928d3a6b6.jpg",
                "from": "bangumi",
                "id": 307056,
                "long_title": "初始的终结与结束的开始",
                "share_url": "https://www.bilibili.com/bangumi/play/ep307056",
                "status": 2,
                "title": "1",
                "vid": ""
            }, {
                "aid": 85577520,
                "badge": "会员",
                "badge_type": 0,
                "cid": 146277911,
                "cover": "http://i0.hdslb.com/bfs/archive/40885f360062380601bbd1339afbba6cf00f90e0.jpg",
                "from": "bangumi",
                "id": 307060,
                "long_title": "哭过喊过便会停止哭泣/勇气的意义",
                "share_url": "https://www.bilibili.com/bangumi/play/ep307060",
                "status": 13,
                "title": "5",
                "vid": ""
            }],
            "id": 39623,
            "title": "正片",
            "type": 0
        },
        "section": [{
            "episodes": [{
                "aid": 80478438,
                "badge": "",
                "badge_type": 0,
                "cid": 137733451,
                "cover": "http://i0.hdslb.com/bfs/archive/c3d8d7b8faa9bb8f14301327df8cf430d31b6d39.jpg",
                "from": "bangumi",
                "id": 304575,
                "long_title": "",
                "share_url": "https://www.bilibili.com/bangumi/play/ep304575",
                "status": 2,
                "title": "PV",
                "vid": ""
            }],
            "id": 41230,
            "title": "PV",
            "type": 1
        }]
    }
}
```

- `main_section`:正片

- `section`:PV

# 参数

- `season_id`
