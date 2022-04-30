import requests

# r = requests.get('https://www.baidu.com/')  # 发送请求
# print(r.status_code)  # 返回状态码
# print(r.text)  # 返回网页源码
# print(r.cookies)  # 返回cookies
# print(r.headers)  # 返回请求头
# print(r.headers['Content-Type'])  # 返回请求头中的Content-Type
# print(r.headers['Content-Length'])  # 返回请求头中的Content-Length...等等等
# print(r.url)  # 返回请求的url
# print(r.encoding)  # 返回网页编码
# print(r.content)  # 返回网页内容
# print(r.json())  # 返回json格式的数据

# 1.对于GET请求,附加额外的信息
# data = {'name': 'germey', 'age': 22}
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.url)  # 返回请求的url
# print(r.text)  # 返回网页源码
# # 如果网页返回的是json格式的数据,可以使用json()方法获取
# print(r.json())

# 2.加入headers信息
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# r = requests.get('http://httpbin.org/get', headers=headers)

# 3.加入cookies信息
cookies = {'name': 'germey'}
r = requests.get('http://httpbin.org/get', cookies=cookies)
print(r.text)
