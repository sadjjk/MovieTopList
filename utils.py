from Douban.config import DoubanVideoTopList
from Bilibili.config import BilibiliVideoTopList


def get_all_top_list():
    all_top_list = []
    all_top_list.extend(
        [{"name": video['name'],
          "name_len": len(video['name']),
          "url": '/bilibili/' + str(index)} for index, video in enumerate(BilibiliVideoTopList)
         ])

    all_top_list.extend(
        [{"name": video['name'],
          "name_len": len(video['name']),
          "url": '/douban/' + str(index)} for index, video in enumerate(DoubanVideoTopList)])

    return all_top_list
