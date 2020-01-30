# 说明

(不确定)

# 示例

- 后街女孩

`http://api.bilibili.com/pgc/view/web/season/user/status?season_id=24567`

```json
{
    "code": 0,
    "message": "success",
    "result": {
        "area_limit": 0,
        "ban_area_show": 1,
        "follow": 0,
        "follow_status": 2,
        "login": 0,
        "paster": {
            "aid": 0,
            "allow_jump": 0,
            "cid": 0,
            "duration": 0,
            "type": 0,
            "url": ""
        },
        "pay": 0,
        "pay_pack_paid": 0,
        "sponsor": 0
    }
}
```

- 超电磁炮T

`http://api.bilibili.com/pgc/view/web/season/user/status?season_id=29325`

```json
{
    "code": 0,
    "message": "success",
    "result": {
        "area_limit": 0,
        "ban_area_show": 1,
        "dialog": {
            "btn_right": {
                "title": "成为大会员",
                "type": "vip"
            },
            "desc": "",
            "title": "开通大会员抢先看"
        },
        "follow": 0,
        "follow_status": 2,
        "login": 0,
        "paster": {
            "aid": 0,
            "allow_jump": 0,
            "cid": 0,
            "duration": 0,
            "type": 0,
            "url": ""
        },
        "pay": 0,
        "pay_pack_paid": 0,
        "sponsor": 0
    }
}
```

# 参数

- `season_id`
