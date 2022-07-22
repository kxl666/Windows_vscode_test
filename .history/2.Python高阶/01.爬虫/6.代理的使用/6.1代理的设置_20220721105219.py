import requests

# 01 request
url = 'http://httpbin.org/get'
proxy = '127.0.0.1:1080'
proxies = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
response = requests.get(url, proxies=proxies)
print(response.text)
# 如果代理需要认证，同样在代理的前面加上用户名密码即可
# proxy = 'user:password@127.0.0.1:1080'

# 使用 SOCKS5 代理
proxies = {'http': f'socks5://{}', 'https': f'socks5://{}'}