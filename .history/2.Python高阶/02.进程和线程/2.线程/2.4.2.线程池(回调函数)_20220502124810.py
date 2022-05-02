import concurrent.futures

urls = ['https://www.kxl666.com/page' + str(i) for i in range(1, 10)]


def craw(url):
    return url


def callback(future):  # 定义回调函数
    print(future.result())


# # 方式1: map函数 阻塞模式
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
#     htmls = pool.map(craw, urls)
#     for html in htmls:
#         print(html)

# print('map is over!')

# 方式2: future模式 非阻塞模式
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    # 创建future对象
    futures = [
        pool.submit(craw, url).add_done_callback(callback) for url in urls
    ]  # 参数是一个一个的传入,不同于map函数
    # 获取future对象的结果
    # for future in concurrent.futures.as_completed(futures):
    #     print(future.result())

print('future is over!')
