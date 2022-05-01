'''
当需要创建的子进程数量不多时,可以直接利用multiprocessing中的Process动态成生多个进程,
但如果是上百甚至上千个目标,手动的去创建进程的工作量巨大,此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时,可以指定一个最大进程数,当有新的请求提交到Pool中时,如果池还没有满,
那么就会创建一个新的进程用来执行该请求;但如果池中的进程数已经达到指定的最大值,那么该请求就会等待,直到池中有进程结束,才会创建新的进程来执行。

阻塞式进程池:
非阻塞式进程池:
'''
import random
import time  # 01
# 有两种方式可以创建进程池,一种是通过multiprocessing.Pool类来创建,另一种是通过concurrent.futures.ProcessPoolExecutor类来创建。
from multiprocessing import Pool

# from concurrent.futures import ThreadPoolExecutor # 02

# 01.非阻塞式进程池


def task(task_name):
    print('{}--->开始任务！'.format(task_name))
    start = time.time()
    time.sleep(random.random() * 2)
    end = time.time()
    print('完成任务！用时：', end - start)
