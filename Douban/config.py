MaxTopVideoNum = 20

UserAgents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
]

DoubanVideoTopList = [
    {
        "name": "豆瓣热门电影",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/movie_hot_gaia/items?start=0&count=50&items_only=1&for_mobile=1&ck=-GIk",
        "referer": "https://m.douban.com/subject_collection/movie_hot_gaia",
        "update_weekday": [1, 2, 3, 4, 5, 6, 7],
        "update_desc": "每天更新"
    },
    {
        "name": "一周口碑电影榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/movie_weekly_best/items?start=0&count=50&items_only=1&for_mobile=1&ck=-GIk",
        "referer": "https://m.douban.com/subject_collection/movie_weekly_best",
        "update_weekday": [6],
        "update_desc": "每周六更新"
    },
    {
        "name": "华语口碑剧集榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_chinese_best_weekly/items?start=0&count=50&items_only=1&for_mobile=1&ck=-GIk",
        "referer": "https://m.douban.com/subject_collection/tv_chinese_best_weekly",
        "update_weekday": [4],
        "update_desc": "每周四更新"
    },
    {
        "name": "全球口碑剧集榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_global_best_weekly/items?start=0&count=50&items_only=1&for_mobile=1&ck=-GIk",
        "referer": "https://m.douban.com/subject_collection/tv_global_best_weekly",
        "update_weekday": [4],
        "update_desc": "每周四更新"
    },
    {
        "name": "国内口碑综艺榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/show_chinese_best_weekly/items?start=0&count=50&items_only=1&for_mobile=1&ck=-GIk",
        "referer": "https://m.douban.com/subject_collection/show_chinese_best_weekly",
        "update_weekday": [2],
        "update_desc": "每周二更新"
    },
    {
        "name": "国外口碑综艺榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/show_global_best_weekly/items?start=0&count=50&items_only=1&for_mobile=1&ck=-GIk",
        "referer": "https://m.douban.com/subject_collection/show_global_best_weekly",
        "update_weekday": [2],
        "update_desc": "每周二更新"
    },
    {
        "name": "华语电影-2020高分榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/EC2A5MRIY/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/EC2A5MRIY?dt_dapp=1",
    },
    {
        "name": "外语电影-2020高分榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/ECIU5HIEQ/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/ECIU5HIEQ?dt_dapp=1",
    },
    {
        "name": "全球电影票房榜",
        "url": "https://www.douban.com/doulist/1274560/",
        "type": "doulist"
    },
    {
        "name": "中二神作动漫",
        "url": "https://www.douban.com/doulist/37754603/",
        "type": "doulist",
        "update_desc": "排名不分先后"
    },
    {
        "name": "日本最佳动画",
        "url": "https://www.douban.com/doulist/45955373/",
        "type": "doulist",
        "update_desc": "排名不分先后"
    },
    {
        "name": "高分动漫电影",
        "url": "https://www.douban.com/doulist/37952767/",
        "type": "doulist",
        "update_desc": "排名不分先后"
    },
    {
        "name": "冷门佳作-2020高分榜",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/ECGY5FDUA/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/ECGY5FDUA?dt_dapp=1",
    },
    {
        "name": "历代奥斯卡获奖影片",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3793/items?start=0&count=50&items_only=1&for_mobile=1&ck=0ul4",
        "referer": "https://m.douban.com/subject_collection/3793?dt_dapp=1",
    },
    {
        "name": "最佳科幻片",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/movie_scifi/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/movie_scifi",
    },
    {
        "name": "最佳动作片",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/movie_action/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/movie_action",
    },
    {
        "name": "最佳爱情片",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/movie_love/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/movie_love",
    },
    {
        "name": "最佳喜剧片",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/movie_comedy/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/movie_comedy",
    },
    {
        "name": "最佳灾难片",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/natural_disasters/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/natural_disasters",
    },
    {
        "name": "网飞系列动画",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/5160/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/5160",
    },
    {
        "name": "速度与激情系列",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3019/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/3019"
    },
    {
        "name": "星球大战系列",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3037/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/3037"
    },
    {
        "name": "漫威宇宙观影顺序",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3194/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/3194?dt_dapp=1"
    },
    {
        "name": "新海诚系列作品",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/1948/items?start=0&count=50&items_only=1&for_mobile=1&ck=0ul4",
        "referer": "https://m.douban.com/subject_collection/1948?dt_dapp=1",
    },
    {
        "name": "今敏系列作品",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/1933/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/1933",
    },
    {
        "name": "伍迪·艾伦系列作品",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/1918/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/1918",
    },
    {
        "name": "名侦探柯南系列",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3167/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/3167?dt_dapp=1",
    },
    {
        "name": "海贼王剧场版系列",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3169/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/3169?dt_dapp=1",
    },
    {
        "name": "火影忍者剧场版系列",
        "url": "https://m.douban.com/rexxar/api/v2/subject_collection/3164/items?start=0&count=50&items_only=1&for_mobile=1",
        "referer": "https://m.douban.com/subject_collection/3164?dt_dapp=1",
    },

]


