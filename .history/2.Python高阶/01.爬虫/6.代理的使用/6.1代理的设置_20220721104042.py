import requests
from zmq import proxy

# 01 request
url = 'http://httpbin.org/get'
proxy = 
response = requests.get(url, proxies=proxy)
print(response.text)
