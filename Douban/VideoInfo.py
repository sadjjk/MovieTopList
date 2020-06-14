'''
根据豆瓣的地址 如https://www.douban.com/movie/subject/27186348/
解析html 获取相关data
算是对豆瓣Video接口剩余参数的补充
'''

# from gevent import monkey
# monkey.patch_all()
import requests
# import gevent
import re
import random
from Douban.config import UserAgents
from Douban.Login import DoubanLogin
from Douban.config import USERNAME,PASSWORD


class DoubanVideoInfo:

    # _,session = DoubanLogin().login(USERNAME,PASSWORD)

    @staticmethod
    def get_html_content(video_id):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            "Host": "movie.douban.com"}

        url = 'https://movie.douban.com/subject/' + str(video_id)

        # response = DoubanVideoInfo.session.get(url, headers=headers)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            content = response.text

            img_id = re.findall(r'<img src=".*?/(p\d+).jpg" alt="图片" />', content)
            pic_url = 'https://img1.doubanio.com/view/photo/photo/public/{}.jpg'.format(
                img_id[0]) if img_id else ''
            description = re.findall(r'"description": "(.*?)"', content,re.S)
            description = description[0] if description else ''

            tags = re.findall(r'<a href="/tag/.*?">(.*?)</a>', content)
            tags = tags[:5] if tags else ''

            return {"pic": pic_url,
                    "description": description,
                    "continuous_tags": tags
                    }


    # @staticmethod
    # def get_video_list_html_content(video_id_list):
    #     '''
    #     使用gevent协程 加快多个页面的爬取
    #     :param url_list:
    #     :return:
    #     '''
    #     jobs = [gevent.spawn(DoubanVideoInfo.get_html_content, video_id) for video_id in video_id_list]
    #     gevent.joinall(jobs)
    #     return [job.value for job in jobs]


#  太慢 速度上和直接获取html内容差不了多少
class DoubanVideoImg:

    @staticmethod
    def get(video_id, num=1):
        url = 'https://api.douban.com/v2/movie/subject/{}/photos?apikey=0df993c66c0c636e29ecbb5344252a4a&start=0&count=10'.format(
            video_id)

        headers = {"User-Agent": random.choice(UserAgents)}

        response = requests.get(url, headers=headers)

        assert response.status_code == 200, '地址:{} 连接异常'.format(url)

        content = response.json()

        return {'pic': [photo['thumb'].replace('m/public', 'photo/public') for photo in content["photos"][:num]][0]}

    # @staticmethod
    # def get_video_list_img(video_id_list):
    #     '''
    #     使用gevent协程 加快多个页面的爬取
    #     :param url_list:
    #     :return:
    #     '''
    #     jobs = [gevent.spawn(DoubanVideoImg.get, video_id) for video_id in video_id_list]
    #     gevent.joinall(jobs)
    #     return [job.value for job in jobs]


if __name__ == '__main__':
    print(DoubanVideoInfo.get_html_content('1439579'))

    # import datetime
    #
    # count = 0
    # while count < 10:
    #     start_time = datetime.datetime.now()
    #     print(start_time)
    #     url_list = ['https://www.douban.com/movie/subject/27186348/', 'https://www.douban.com/movie/subject/33420285/',
    #                 'https://www.douban.com/movie/subject/30244174/', 'https://www.douban.com/movie/subject/34825471/',
    #                 'https://www.douban.com/movie/subject/34977898/', 'https://www.douban.com/movie/subject/30318116/',
    #                 'https://www.douban.com/movie/subject/34968329/', 'https://www.douban.com/movie/subject/30402296/',
    #                 'https://www.douban.com/movie/subject/30176393/', 'https://www.douban.com/movie/subject/35055448/',
    #                 'https://www.douban.com/movie/subject/30314127/', 'https://www.douban.com/movie/subject/30331959/',
    #                 'https://www.douban.com/movie/subject/30292777/', 'https://www.douban.com/movie/subject/30410114/',
    #                 'https://www.douban.com/movie/subject/30271841/', 'https://www.douban.com/movie/subject/30372314/',
    #                 'https://www.douban.com/movie/subject/30166972/', 'https://www.douban.com/movie/subject/27089612/',
    #                 'https://www.douban.com/movie/subject/25842038/', 'https://www.douban.com/movie/subject/30211998/',
    #                 'https://www.douban.com/movie/subject/30401849/', 'https://www.douban.com/movie/subject/34904937/',
    #                 'https://www.douban.com/movie/subject/30405087/', 'https://www.douban.com/movie/subject/25887288/',
    #                 'https://www.douban.com/movie/subject/34678128/', 'https://www.douban.com/movie/subject/6538866/']
    #
    #     DoubanVideoInfo.get_video_list_html_content(url_list)
    #     end_time = datetime.datetime.now()
    #     print(end_time)
    #     print(end_time - start_time)
    #     count += 1

    # import datetime
    #
    # print(datetime.datetime.now())
    # DoubanVideoImg.get('34968314')
    # print(datetime.datetime.now())
