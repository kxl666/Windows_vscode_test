# 1.使用线程池proxy_pool,进入目录python proxyPool.py server & python proxyPool.py schedule
import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


url = 'http://httpbin.org/get'
proxy = get_proxy()['proxy']
# print(proxy)
proxies = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
response = requests.get(url, proxies=proxies)
print(response.text)

# 2.使用ProxyPool