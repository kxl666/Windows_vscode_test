import requests
from zmq import proxy

# 01 request
url = 'http://httpbin.org/get'
proxy = '127.0.0.1:1080'
proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
response = requests.get(url, proxies=proxy)
print(response.text)
