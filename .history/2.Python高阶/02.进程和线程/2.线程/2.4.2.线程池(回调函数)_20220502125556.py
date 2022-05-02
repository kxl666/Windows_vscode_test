#
''' 
    1.直接用映射map可以简化代码，不需要使用shutdown
    2.没有回调函数，直接收集函数运行结果
'''
import concurrent.futures

urls = ['https://www.kxl666.com/page' + str(i) for i in range(1, 10)]


def craw(url):
    return url


# 方式2: future模式 非阻塞模式的对调函数
def callback(future):  # 定义回调函数
    print(future.result())


# 方式2: future模式 非阻塞模式
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    # 创建future对象
    futures = [
        pool.submit(craw, url).add_done_callback(callback) for url in urls
    ]
print('future is over!')
