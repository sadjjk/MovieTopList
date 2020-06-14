MaxTopVideoNum = 20

BilibiliVideoTopList = [
    {
        "name": "哔哩哔哩全站榜",
        "url": "https://api.bilibili.com/x/web-interface/ranking?rid=0&day=3&type=1&arc_type=0&jsonp=jsonp&callback=__jp1",
        "referer": "https://www.bilibili.com/ranking/bangumi/13/0/3",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新"
    },
    {
        "name": "哔哩哔哩电影榜",
        "url": "https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=2",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新"
    },
    {
        "name": "动漫追番榜",
        "url": "https://api.bilibili.com/pgc/season/index/result?order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新",
        "type": "bangumi"
    },
    {
        "name": "动漫高分榜",
        "url": "https://api.bilibili.com/pgc/season/index/result?order=4&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新",
        "type": "bangumi"
    },
    {
        "name": "动漫播放榜",
        "url": "https://api.bilibili.com/pgc/season/index/result?order=2&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新",
        "type": "bangumi"
    },
    {
        "name": "动漫新番榜",
        "url": "https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新",
        "type": "bangumi"
    },
    {
        "name": "影视纪录片榜",
        "url": "https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=3",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新",
        "type": "bangumi"
    },
]
