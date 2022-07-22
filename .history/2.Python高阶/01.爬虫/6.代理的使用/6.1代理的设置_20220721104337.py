import requests
from zmq import proxy

# 01 request
url = 'http://httpbin.org/get'
proxys = '127.0.0.1:1080'
proxies = {'http': f'http://{proxys}', 'https': f'https://{proxys}'}
response = requests.get(url, proxies=proxies)
print(response.text)
