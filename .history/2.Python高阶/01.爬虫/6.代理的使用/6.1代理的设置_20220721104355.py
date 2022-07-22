import requests

# 01 request
url = 'http://httpbin.org/get'
proxy = '127.0.0.1:1080'
proxies = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
response = requests.get(url, proxies=proxies)
print(response.text)
