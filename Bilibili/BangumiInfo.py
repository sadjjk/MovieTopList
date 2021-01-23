'''

根据bilibili番剧的地址 如https://www.bilibili.com/bangumi/media/md22718131/
解析html 获取相关data
对剩余信息的补充
'''

from gevent import monkey
monkey.patch_all()
import requests
import gevent
import re
import json


class BangumiInfo:

    @staticmethod
    def get_html_content(media_id,season_id):

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


        if not media_id:
            seaon_url = 'https://www.bilibili.com/bangumi/play/ss' + str(season_id)
            response = requests.get(seaon_url, headers=headers)
            assert response.status_code == 200, '地址:{} 连接异常'.format(seaon_url)

            media_id = re.findall(r'//www.bilibili.com/bangumi/media/md(\d+)/',response.text)
            assert media_id,'{}中找不到media_id'.format(seaon_url)
            media_id = media_id[0]

        mdeia_url = 'https://www.bilibili.com/bangumi/media/md' + str(media_id)

        response = requests.get(mdeia_url, headers=headers)
        assert response.status_code == 200, '地址:{} 连接异常'.format(mdeia_url)
        content = response.text

        description = re.findall(r'"evaluate":"(.*?)"', content, re.S)
        description = description[0].replace('──','').replace('——','').replace('\\n',' ') if description else ''
        tags_string = re.findall(r'"styles":(\[.*?\])', content, re.S)
        tags_list = json.loads(tags_string[0]) if tags_string else ''
        tags = [tag['name'] for tag in tags_list]

        actors = re.findall(r'"actors":"(.*?)"', content, re.S)
        actors = actors[0] if actors else ''

        card_subtitle = ' / '.join(actors.split('\\n')[:5])


        if not season_id:
            season_id = re.findall(r'"season_id":(\d+)', content)
            season_id = season_id[0] if season_id else ''

        season_api_url = 'https://api.bilibili.com/pgc/web/season/section?season_id=' + str(season_id)
        response = requests.get(season_api_url, headers=headers)
        assert response.status_code == 200, '地址:{} 连接异常'.format(season_api_url)
        season_content = response.json()

        section = season_content['result'].get('main_section')
        section = section if section else season_content['result'].get('section')[0]
        pic_url = section['episodes'][0]['cover']


        return {"card_subtitle": card_subtitle,
                "pic": pic_url,
                "description": description,
                "continuous_tags": tags
                }

    @staticmethod
    def get_video_list_html_content(id_list):
        '''
        使用gevent协程 加快多个页面的爬取
        :param url_list:
        :return:
        '''
        jobs = [gevent.spawn(BangumiInfo.get_html_content, media_id,season_id) for (media_id,season_id) in id_list]
        gevent.joinall(jobs)
        return [job.value for job in jobs]


if __name__ == '__main__':
    print(BangumiInfo.get_html_content(22718131,32982))
    # print(BangumiInfo.get_video_list_html_content([22718131]))
