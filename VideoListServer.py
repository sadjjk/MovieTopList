from flask import Flask, render_template, redirect
from Bilibili.VideoTop import BilibiliVideoTop
from Douban.VideoTop import DoubanVideoTop
from utils import get_all_top_list
app = Flask(__name__, static_url_path='')


@app.route('/')
@app.route('/index')
def index():
    return redirect('/bilibili/0')


@app.route("/douban/<int:index>", methods=['GET'])
def get_douban_video_list(index):
    all_top_list = get_all_top_list()
    list_info_dict = DoubanVideoTop.check_update_get(index)
    content = list_info_dict.get('content')
    name = list_info_dict.get('name')
    update_desc = list_info_dict.get('update_desc')

    origin_img_url = "https://img3.doubanio.com/f/sns/0f9e2dbca60b52f595ddbc02073cb4bb879ed1c9/pics/nav/logo_db@2x.png"
    origin_url = "https://www.douban.com"

    return render_template("video.html",
                           content=content,
                           top_name=name,
                           update_desc=update_desc,
                           all_list=all_top_list,
                           origin_img_url=origin_img_url,
                           origin_url=origin_url
                           )


@app.route("/bilibili/<int:index>", methods=['GET'])
def get_bilibili_video_list(index):
    all_top_list = get_all_top_list()
    list_info_dict = BilibiliVideoTop.check_update_get(index)
    content = list_info_dict.get('content')
    name = list_info_dict.get('name')
    update_desc = list_info_dict.get('update_desc')

    origin_img_url = "/images/bilibili_logo.png"
    origin_url = "https://www.bilibili.com"

    return render_template("video.html",
                           content=content,
                           top_name=name,
                           update_desc=update_desc,
                           all_list=all_top_list,
                           origin_img_url=origin_img_url,
                           origin_url=origin_url
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)
