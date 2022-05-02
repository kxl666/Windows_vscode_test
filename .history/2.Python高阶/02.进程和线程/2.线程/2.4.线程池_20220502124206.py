# 使用线程池的好处：
#   1、提升性能:因为减去了大量新建、终止线程的开销，重用了线程资源;
#   2、适用场景:适合处理突发性大量请求或需要大量线程完成任务、但实际任务处理时间较短
#   3、防御功能:能有效避免系统因为创建线程过多，而导致系统负荷过大相应变慢等问题
#   4、代码优势:使用线程池的语法比自己新建线程执行线程更加简洁

# 有两种方式可以创建进程池,一种是通过multiprocessing.Pool类来创建,另一种是通过concurrent.futures.ThreadPoolExecutor类来创建
# concurrent.futures.ThreadPoolExecutor使用方式：
#     1.用法 map函数，很简单注意map的结果和入参是顺序对应的
#     2.用法2: future模式,更强大注意如果用 as_completed顺序是不定的

import concurrent.futures

urls = ['https://www.kxl666.com/page' + str(i) for i in range(1, 10)]


def craw(url):
    return url


def callback(future):  # 定义回调函数
    print(future.result())


# 方式1: map函数
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    htmls = pool.map(craw, urls).add
    for html in htmls:
        print(html)

print('map is over!')

# 方式2: future模式
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    # 创建future对象
    futures = [pool.submit(craw, url) for url in urls]  # 参数是一个一个的传入,不同于map函数
    # 获取future对象的结果
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

print('future is over!')
