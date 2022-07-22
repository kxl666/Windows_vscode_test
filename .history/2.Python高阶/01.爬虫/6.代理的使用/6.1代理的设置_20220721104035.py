import requests

# 01 request
url = 'http://httpbin.org/get'
pro
response = requests.get(url, proxies=proxy)
print(response.text)
