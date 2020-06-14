import requests


class DoubanLogin():
    def __init__(self):

        self.session = requests.Session()

    '''登录函数'''

    def login(self, username, password):

        self.__initializePC()
        self.session.get(self.home_url)
        # 模拟登录
        data = {
            'ck': '',
            'name': username,
            'password': password,
            'remember': 'true',
            'ticket': ''
        }
        res = self.session.post(self.login_url, data=data)
        res_json = res.json()
        # 登录成功
        if res_json['status'] == 'success':
            print('[INFO]: Account -> %s, login successfully...' % username)
            infos_return = {'username': username}
            infos_return.update(res_json)
            return infos_return, self.session
        # 账号或密码错误
        elif res_json['status'] == 'failed' and res_json['message'] == 'unmatch_name_password':
            raise RuntimeError('Account -> %s, fail to login, username or password error...' % username)
        # 其他错误
        else:
            raise RuntimeError(res_json.get('description'))

    '''初始化PC端'''

    def __initializePC(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Host': 'accounts.douban.com',
            'Origin': 'https://accounts.douban.com',
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
        }
        self.home_url = 'https://www.douban.com/'
        self.login_url = 'https://accounts.douban.com/j/mobile/login/basic'
        self.session.headers.update(self.headers)

if __name__ == '__main__':
    DoubanLogin().login('*****', '****')
