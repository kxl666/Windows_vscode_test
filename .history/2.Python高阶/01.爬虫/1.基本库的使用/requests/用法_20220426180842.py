import requests

r = requests.get('https:I/www.baidu.com/')
print(r.status_code)  # 返回状态码
# print(r.text)  # 返回网页源码
print(r.cookies)  # 返回cookies
