import concurrent.futures

urls = ['https://www.kxl666.com/page' + str(i) for i in range(1, 10)]


def craw(url):
    return url


# 方式1: map函数 阻塞模式的对调函数
def callback(htmls):
    for html in htmls:
        print(html)


# 方式2: future模式 非阻塞模式的对调函数
# def callback(future):  # 定义回调函数
#     print(future.result())

# 方式1: map函数 阻塞模式
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    htmls = pool.map(craw, urls).add_done_callback(callback)

print('map is over!')

# 方式2: future模式 非阻塞模式
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
#     # 创建future对象
#     futures = [
#         pool.submit(craw, url).add_done_callback(callback) for url in urls
#     ]
# print('future is over!')
