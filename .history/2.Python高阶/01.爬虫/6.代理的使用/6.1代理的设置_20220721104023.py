import requests

# 01 request
url = 'http://httpbin.org/get'

response = requests.get(url, proxies=proxy)
print(response.text)
