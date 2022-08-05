# 1.使用线程池proxy_pool,进入目录python proxyPool.py server & python proxyPool.py schedule
import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


# your spider code


def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get('http://httpbin.org/get',
                                proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
    return None


# url = 'http://httpbin.org/get'
# proxy = get_proxy()['proxy']
# # print(proxy)
# proxies = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
# response = requests.get(url, proxies=proxies)
# print(response.text)
if __name__ == '__main__':
    getHtml()
