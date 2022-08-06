import requests
from lxml import etree


class Login(object):

    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()
        self.session.keep_alive = False

    def token(self):
        requests.packages.urllib3.disable_warnings()  # 忽略警告
        response = self.session.get(self.login_url,
                                    headers=self.headers,
                                    verify=False)
        selector = etree.HTML(response.text)
        token = selector.xpath(
            '//*[@id="login"]/div[4]/form/input[1]/@value')[0]
        print(token)
        # response.close()
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url,
                                     data=post_data,
                                     headers=self.headers)
        response.close()
        print(response.status_code)
        # if response.status_code == 200:
        #     self.dynamics(response.text)

        # response = self.session.get(self.logined_url, headers=self.headers)
        # if response.status_code == 200:
        #     self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//*[@id="feed-item-0"]/div/div')
        for item in dynamics:
            # dynamic = ' '.join(
            #     item.xpath('.//div[@class="title"]//text()')).strip()
            # dynamic = item.xpath('./section[1]/text()')
            # print(dynamic)
            print(item)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath(
            '//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name, email)


if __name__ == "__main__":
    login = Login()
    login.login(email='2244951869@qq.com', password='13545548310kqf')
