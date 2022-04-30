import requests

r = requests.get('https://www.baidu.com/')  # 发送请求
# print(r.status_code)  # 返回状态码
# print(r.text)  # 返回网页源码
# print(r.cookies)  # 返回cookies
# print(r.headers)  # 返回请求头
# print(r.url)  # 返回请求的url
# print(r.encoding)  # 返回网页编码
print(r.content)  # 返回网页内容
# print(r.json())  # 返回json格式的数据
