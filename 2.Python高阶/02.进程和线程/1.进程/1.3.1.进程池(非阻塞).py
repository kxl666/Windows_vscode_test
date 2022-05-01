'''
当需要创建的子进程数量不多时,可以直接利用multiprocessing中的Process动态成生多个进程,
但如果是上百甚至上千个目标,手动的去创建进程的工作量巨大,此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时,可以指定一个最大进程数,当有新的请求提交到Pool中时,如果池还没有满,
那么就会创建一个新的进程用来执行该请求;但如果池中的进程数已经达到指定的最大值,那么该请求就会等待,直到池中有进程结束,才会创建新的进程来执行。

阻塞式进程池: 非阻塞式:全部添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务完成之后才调用。
非阻塞式进程池:
'''
import os
import random
import time  # 01
# 有两种方式可以创建进程池,一种是通过multiprocessing.Pool类来创建,另一种是通过concurrent.futures.ProcessPoolExecutor类来创建。
from multiprocessing import Pool

# from concurrent.futures import ThreadPoolExecutor # 02

# 01.非阻塞式进程池


def task(task_name):
    print('{}--->开始任务！'.format(task_name))
    start = time.time()
    time.sleep(random.random() * 2)  # 进程等待的时候,进入阻塞状态,等待被唤醒,然后就绪状态,等待执行
    end = time.time()
    print('{}-->{} 完成任务！用时：{}'.format(task_name, os.getpid(), end - start))


if __name__ == '__main__':
    pool = Pool(5)  # 创建一个进程池,最大进程数为5

    tasks = ['听音乐', '打游戏', '吃饭', '跑步', '睡觉', '撸铁']
    for things in tasks:
        pool.apply_async(
            task,
            args=(things, ))  # 异步执行任务,apply_async()方法是非阻塞式的,apply()方法是阻塞式的。
    # 由于是非阻塞模式,输出的结果中,并不会 先都输出 {}--->开始任务！ 然后都再输出{}-->{} 完成任务！用时：{}'
    pool.close()  # 关闭进程池,不再接受新的请求
    pool.join()  # 等待所有子进程执行完毕

    print('主进程结束！')
