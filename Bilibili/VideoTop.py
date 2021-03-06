'''
根据接口获取豆瓣榜单数据
'''
from cacheout import Cache
from datetime import datetime
from Bilibili.BangumiInfo import BangumiInfo
from Bilibili.config import *
import requests
import re
import json

class BilibiliVideoTop:
    cache = Cache(maxsize=256, ttl=0)
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
        try:
            json_content = response.json()
        except:
            content = re.findall(r"_jp\d\((.*)\)",response.text)
            content = content[0] if content else '{}'
            json_content = json.loads(content)

        return json_content

    @staticmethod
    def get(list_index):

        if BilibiliVideoTop.cache.has(list_index):
            return BilibiliVideoTop.cache.get(list_index)
        else:

            this_top_list = BilibiliVideoTopList[list_index]

            assert this_top_list, '第{}个榜单不存在 请检查!'.format(list_index + 1)

            url = this_top_list["url"]
            referer = this_top_list.get("referer",None)
            response = BilibiliVideoTop.get_request(url, referer)
            content_list = response.get('data').get('list') if response.get('data') else response.get('result').get('list')

            content = []
            for index, video in enumerate(content_list):

                if index < MaxTopVideoNum:
                    video_info = {}

                    if video.get('link'):
                        video_info['url'] = video.get('link')
                    elif video.get('url'):
                        video_info['url'] = video.get('url')
                    else:
                        video_info['url'] = 'https://www.bilibili.com/video/' + video.get('bvid')

                    if video.get('order'):
                        video_info['rate'] = video.get('order')
                    elif video.get('author'):
                        video_info['rate'] = video.get('author')
                    else:
                        video_info['rate'] = video.get('desc','')

                    video_info['index'] = index + 1
                    video_info['title'] = video.get('title')

                    video_info['post'] = video.get('cover','/images/bilibili_post.jpg')
                    video_info['media_id'] = video.get('media_id',None)
                    video_info['season_id'] = video.get('season_id',None)

                    if video.get('new_ep'):
                        video_info['pic'] = video['new_ep']['cover']
                    elif this_top_list.get('type') != 'bangumi':
                        video_info['pic'] = video.get('pic')

                    content.append(video_info)

            if this_top_list.get('type') == 'bangumi':
                extra_content = BangumiInfo.get_video_list_html_content([(i['media_id'],i['season_id']) for i in content])
                content = [dict(extra_video_info,**video_info) for video_info, extra_video_info in
                           zip(content, extra_content)]

            list_info_dict = {
                "content": content,
                "name": this_top_list.get('name'),
                "update_desc": this_top_list.get('update_desc')
            }

            BilibiliVideoTop.cache.set(list_index, list_info_dict)

            return list_info_dict

    @staticmethod
    @day_cache.memoize(ttl=12*60*60)
    def check_update_get(list_index):
        weekday_list = BilibiliVideoTopList[list_index].get('update_weekday')
        if weekday_list and (datetime.now().weekday()+1) in weekday_list and BilibiliVideoTop.cache.has(list_index):
            BilibiliVideoTop.cache.delete(list_index)
        return BilibiliVideoTop.get(list_index)


if __name__ == '__main__':

    print(datetime.now())
    dTop = BilibiliVideoTop(0)
    print(dTop.get())
    print(datetime.now())

