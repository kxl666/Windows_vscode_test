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
# print(r.content)  # 返回网页内容,爬取图片时用到,返回的是二进制
# print(r.json())  # 返回json格式的数据
# print(r.history)  # 返回请求历史记录

# 1.对于GET请求,附加额外的信息
# data = {'name': 'germey', 'age': 22}
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.url)  # 返回请求的url
# print(r.text)  # 返回网页源码
# # 如果网页返回的是json格式的数据,可以使用json()方法获取
# print(r.json())

# 2.对于POST请求,附加额外的信息
# data = {'name': 'germey', 'age': 22}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)

# 3.加入headers信息
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# r = requests.get('http://httpbin.org/get', headers=headers)

# 4.加入cookies信息
# 4.1 创建cookies对象
# cookies = {'name': 'germey'}
# r = requests.get('http://httpbin.org/get', cookies=cookies)
# print(r.text)
# 4.2 将cookies写入headers中
# headers = {
#     'Cookie':
#     '_zap=ef86de08-6843-4093-b0f9-7257827422e8;d_c0="AEAfQFTLyBSPToUaYE0PZiwbhYf_8uwyUI4=|1649852457"; captcha_session_v2=2|1:0|10:1649852488|18:captcha_session_v2|88:ZTV5RFkvNWp5WGJWcE1ydzZTdWZFVnJnNUxjZHNpSmJqbzNLbjZQczlPdkFWN3UyemlMdFZiYlJKU0diYnkwNA==|4be1c768e463d6e66f185f3b30b99314c06062451b80672a9bd49a963d817a53; captcha_ticket_v2=2|1:0|10:1649852495|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfRHg1VS14VDI4WVpoMnNLV08yWnNJTkVWVFpERHZTQVY0XzE3T056b0NiNG1FUVpOcVRJbmQuTENQSkFTdzE0MGtmdUE2aUNHVU1zNUIwNGlBQXZIa1JFLWRlZkstNXNmdy1pQ2JmTTA1Uy1LRjAwUy5hSFpua1pqc2pSeUVwbVRiZ3NTZDBfNnRpVExtVk9fb095TVZzMlVwUkV0Q2J3VC1SNjJSY2lwUGlNWE9rOWNnZHBJOE9iV015Zl9DWDZPck1zdlBkWnAub3RRUEtORjV2TDAtWHBhNC1vQmhIcHBvb1I1cHBSRXhzTWhDd3RTbEJGbVRNMHZmemRpeU9CS3Y1S2JYWG9PWEd3bEpvdTk0Smg3cXBfdEVRZUt0LkF6MkxYT0tyLVpxSE4tV3ladm1CUnVIbXc2a3ZmLkQ4QU5neFNxQXNUcDBpaHZLdUVHZ3YwVFJYU3ZiS09zTEFkRHUxcDJuUkZFQnF0VzllS1FKakhZNnp5TzlVdUdSVmN6TUd2NGNfX0wyMThOS1VVdkxHUDUyWV9sQ2lNTnA2WEUwbmUwUXFNRElzSi1jYXRudXIxVWxvV2ZZQkg4ZHUwRWVDT2xkc0poT2tuVGRTVjZqZXRUUmJ5SlNGSjZkMlI4NkRUcDFlaEVZMjJwYkU3Q0x0OUViejh5NHlaMyJ9|88152fdc14056d2e42e3d0834f2dbbc6342fe51a4eee7e89f47c34a557c47663;z_c0=2|1:0|10:1649852495|4:z_c0|92:Mi4xNnlhNUJnQUFBQUFBUUI5QVZNdklGQ1lBQUFCZ0FsVk5UdzVFWXdBcUZEUlNiUEdFRkYzejlINnhGeU9YS0pUSXdB|9227d838ba20ebbce63a3990675aa55dfc63c27a83e174cbb8ba64c5a8c082f7;_xsrf=215b7e8c-a064-4580-aaa6-93dd5495440e;Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1649861635,1649940949,1650029764,1650030657;q_c1=68a1457911234f2584045549235b2584|1650109293000|1650109293000;Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1650972634;tst=r;NOT_UNREGISTER_WAITING=1; SESSIONID=KhuOdyVnNyMYD5zlT25QJefPTP6AObfgwQZobaH8H6t;JOID=UV4SCkvWihTntYexHtxsgH7oRn8OmONvodL75n6b9liw-LHOcw5SdI-zg74Z9XQqZmkVb8YKwrvxfiuom2xviZk=;osd=VV4UAELSihLtvIOxGNZlhH7uTHYKmOVlqNb74HSS8li28rjKcwhYfYuzhbQQ8XQsbGARb8AAy7_xeCGhn2xpg5A=;KLBRSID=81978cf28cf03c58e07f705c156aa833|1650972637|1650972632',
#     'Host':
#     'www.zhihu.com',
#     'User-Agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/', headers=headers)
# print(r.text)
# 4.3.1 将cookies写入文件
# with open('cookies.txt', 'w') as f:
#     f.write(r.cookies.get_dict())
# 4.3.2 将cookies写入文件
# with open('cookies.txt', 'r') as f:
#     cookies = json.load(f)
# r = requests.get('http://httpbin.org/cookies', cookies=cookies)
# print(r.text)
# 4.4 以通过 cookies 参数来设置，不过这样就需要构造 RequestsCookieJa 对象，而且要分割一下 cookies

# 5.文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# 6.设置超时时间
# r = requests.get('http://httpbin.org/get', timeout=1)
# print(r.text)
