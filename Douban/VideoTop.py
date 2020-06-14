'''
根据接口获取豆瓣榜单数据
'''
from Douban.VideoDoulist import VideoDoulist
from cacheout import Cache
from datetime import datetime
from Douban.config import *

import requests


class DoubanVideoTop:
    cache = Cache(maxsize=256, ttl=60*12*60*60)
    day_cache = Cache()

    @staticmethod
    def get_request(url, referer=None):

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        if referer:
            headers["Referer"] = referer

        response = requests.get(url, timeout=5, headers=headers)

        if response.status_code != 200:
            assert AssertionError('URL:{} \n'
                                  '连接异常'.format(url))
        return response.json()

    @staticmethod
    def get(list_index):

        if DoubanVideoTop.cache.has(list_index):
            return DoubanVideoTop.cache.get(list_index)
        else:

            this_top_list = DoubanVideoTopList[list_index]

            assert this_top_list, '第{}个榜单不存在 请检查!'.format(list_index + 1)

            url = this_top_list["url"]
            referer = this_top_list.get("referer", None)

            if this_top_list.get('type') == 'doulist':
                subject_collection_items = VideoDoulist.get_all_html_content(url)
            else:
                response = DoubanVideoTop.get_request(url, referer)
                subject_collection_items = response.get('subject_collection_items')

            content = []
            for index, video in enumerate(subject_collection_items):

                video_info = {}
                video_info['id'] = video.get('id')
                video_info['index'] = index + 1
                video_info['url'] = video.get('url').replace('m.douban.com', 'www.douban.com')
                video_info['title'] = video.get('title')
                video_info['rate'] = video.get('rating').get('value')
                video_info['card_subtitle'] = video.get('card_subtitle')

                video_info['post'] = video.get('pic').get('normal') if video.get('pic') else video.get('cover').get(
                    'url')

                tags = video.get('tags')
                video_info["manual_tags"] = [tag.get('name') for tag in tags if
                                             tag['type'] == 'manual'] if tags else []
                video_info["continuous_tags"] = [tag.get('name') for tag in tags if
                                                 tag['type'] == 'continuous'] if tags else []
                video_info['description'] = video.get('description','')
                video_info['pic'] = video.get('photos')[0] if video.get('photos') else video_info['post']

                content.append(video_info)

                if index > MaxTopVideoNum and this_top_list.get('update_weekday'):
                    break

            list_info_dict = {
                "content": content,
                "name": this_top_list.get('name'),
                "update_desc": this_top_list.get('update_desc')
            }

            DoubanVideoTop.cache.set(list_index, list_info_dict)

            return list_info_dict

    @staticmethod
    @day_cache.memoize(ttl=12 * 60 * 60)
    def check_update_get(list_index):

        weekday_list = DoubanVideoTopList[list_index].get('update_weekday')
        if weekday_list and (datetime.now().weekday() + 1) in weekday_list and DoubanVideoTop.cache.has(list_index):
            DoubanVideoTop.cache.delete(list_index)
        return DoubanVideoTop.get(list_index)


if __name__ == '__main__':
    print(datetime.now())
    dTop = DoubanVideoTop(9)
    print(dTop.get())
    print(datetime.now())
