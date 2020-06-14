'''
豆瓣自制Doulist网页解析
'''
from gevent import monkey
monkey.patch_all()
import gevent
import requests
import re
from itertools import chain


class VideoDoulist:

    @staticmethod
    def get_html_content(url):
        headers = {
            "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            "Host": "m.douban.com"
        }

        response = requests.get(url, headers=headers)

        pattern = r'<li>.*?<a href="(.*?)">.*?<img src="(.*?)" alt="(.*?)">.*?data-rating="(.*?)".*?<div class="meta">(.*?)</div>(.*?)</li>'
        result = re.findall(pattern, response.text, re.S)

        subject_collection_items = []
        if result:
            for item in result:
                url = item[0]
                url = url if url.startswith('https://www.douban.com') else 'https://www.douban.com' + url
                cover = {"url": item[1].replace('s_ratio_poster','l_ratio_poster')}
                title = item[2]
                rating = {"value": str(float(item[3]) / 10)}
                card_subtitle = item[4].strip()

                # 有的有评语 有的没有
                description = re.search(r'<div class="recommend">(.*?)</div>',item[5],re.S)
                if description:
                    description = description.group(1).strip()

                content = {
                    "url": url,
                    "cover": cover,
                    "title": title,
                    "rating": rating,
                    "card_subtitle": card_subtitle
                }
                if description:
                    content['description'] = description
                subject_collection_items.append(content)

        return subject_collection_items

    # 获取多页
    @staticmethod
    def get_all_html_content(url,page=4):
        url_list = [url+'?start={}'.format(i*25) for i in range(page)]

        jobs = [gevent.spawn(VideoDoulist.get_html_content, url) for url in url_list]
        gevent.joinall(jobs)
        return chain(*[job.value for job in jobs])




if __name__ == '__main__':
    # print(VideoDoulist.get_all_html_content('https://www.douban.com/doulist/37952767/'))
    print(VideoDoulist.get_html_content('https://www.douban.com/doulist/37952767/'))
    print(VideoDoulist.get_html_content('https://www.douban.com/doulist/45955373/'))
