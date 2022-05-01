# 使用线程池的好处：
#   1、提升性能:因为减去了大量新建、终止线程的开销，重用了线程资源;
#   2、适用场景:适合处理突发性大量请求或需要大量线程完成任务、但实际任务处理时间较短
#   3、防御功能:能有效避免系统因为创建线程过多，而导致系统负荷过大相应变慢等问题
#   4、代码优势:使用线程池的语法比自己新建线程执行线程更加简洁

#  使用方式：
#     1.用法 map函数，很简单注意map的结果和入参是顺序对应的
#     2.用法2: future模式,更强大注意如果用 as_completed顺序是不定的

import concurrent.futures

urls = ['https://www.kxl666.com/page' + str(i) for i in range(1, 10)]


def craw(url):
    return len(url)


print(list(map(craw, urls)))