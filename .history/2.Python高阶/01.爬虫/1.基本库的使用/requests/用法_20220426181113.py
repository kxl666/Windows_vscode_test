import requests

# header = {
#     'User-Agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
# }
r = requests.get('https://www.baidu.com/')
print(r.status_code)  # 返回状态码
print(r.text)  # 返回网页源码
print(r.cookies)  # 返回cookies
