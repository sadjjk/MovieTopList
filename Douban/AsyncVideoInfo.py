'''
使用Async异步 加快多个页面的爬取
'''

import aiohttp
import asyncio
import re


class DoubanAsyncVideoInfo:

    # 异步HTTP请求
    @staticmethod
    async def fetch(session, url):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        async with session.get(url, headers=headers) as response:
            return await response.text()

    # 解析网页
    @staticmethod
    async def parser(text):
        # 利用正则表达式解析网页
        img_id = re.findall(r'<img src=".*?/(p\d+).jpg" alt="图片" />', text)
        pic_url = 'https://img1.doubanio.com/view/photo/photo/public/{}.jpg'.format(
            img_id[0]) if img_id else ''
        description = re.findall(r'"description": "(.*?)"', text)
        description = description[0] if description else ''

        video_info = {"pic": pic_url,
                      "description": description
                      }
        return video_info

    @staticmethod
    async def get_html_content(url):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            html = await DoubanAsyncVideoInfo.fetch(session, url)
            return await DoubanAsyncVideoInfo.parser(html)

    @staticmethod
    def get_video_list_html_content(url_list):
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(DoubanAsyncVideoInfo.get_html_content(url)) for url in url_list]
        tasks = asyncio.gather(*tasks)
        loop.run_until_complete(tasks)
        return tasks.result()


if __name__ == '__main__':

    import datetime

    count = 0
    while count < 10:
        start_time = datetime.datetime.now()
        print(start_time)
        url_list = ['https://www.douban.com/movie/subject/27186348/', 'https://www.douban.com/movie/subject/33420285/',
                    'https://www.douban.com/movie/subject/30244174/', 'https://www.douban.com/movie/subject/34825471/',
                    'https://www.douban.com/movie/subject/34977898/', 'https://www.douban.com/movie/subject/30318116/',
                    'https://www.douban.com/movie/subject/34968329/', 'https://www.douban.com/movie/subject/30402296/',
                    'https://www.douban.com/movie/subject/30176393/', 'https://www.douban.com/movie/subject/35055448/',
                    'https://www.douban.com/movie/subject/30314127/', 'https://www.douban.com/movie/subject/30331959/',
                    'https://www.douban.com/movie/subject/30292777/', 'https://www.douban.com/movie/subject/30410114/',
                    'https://www.douban.com/movie/subject/30271841/', 'https://www.douban.com/movie/subject/30372314/',
                    'https://www.douban.com/movie/subject/30166972/', 'https://www.douban.com/movie/subject/27089612/',
                    'https://www.douban.com/movie/subject/25842038/', 'https://www.douban.com/movie/subject/30211998/',
                    'https://www.douban.com/movie/subject/30401849/', 'https://www.douban.com/movie/subject/34904937/',
                    'https://www.douban.com/movie/subject/30405087/', 'https://www.douban.com/movie/subject/25887288/',
                    'https://www.douban.com/movie/subject/34678128/', 'https://www.douban.com/movie/subject/6538866/']

        DoubanAsyncVideoInfo.get_video_list_html_content(url_list)

        end_time = datetime.datetime.now()
        print(end_time)
        print(end_time - start_time)
        count += 1
