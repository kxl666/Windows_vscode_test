import os
import random
import time
from multiprocessing import Pool


# 01.非阻塞式进程池 + 回调函数
def task(task_name):
    print('{}--->开始任务！'.format(task_name))
    start = time.time()
    time.sleep(random.random() * 2)  # 进程等待的时候,进入阻塞状态,等待被唤醒,然后就绪状态,等待执行
    end = time.time()
    return '{}-->{} 完成任务！用时：{}'.format(task_name, os.getpid(), end - start)


container = []


def callback(task_name):
    container.append(task_name)


if __name__ == '__main__':
    pool = Pool(5)  # 创建一个进程池,最大进程数为5

    tasks = ['听音乐', '打游戏', '吃饭', '跑步', '睡觉', '撸铁']
    for task_name in tasks:
        pool.apply_async(task, args=(task_name, ), callback=callback)

    pool.close()  # 关闭进程池,不再接受新的请求
    pool.join()  # 等待所有子进程执行完毕

    for task_name in container:
        print(task_name)

    print('主进程结束！')
