# 多进程
"""
进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。
在早期面向进程设计的计算机结构中，进程是程序的基本执行实体;在当代面向线程设计的计算机结构中，进程是线程的容器。
程序是指令、数据及其组织形式的描述，进程是程序的实体。
· 优点:
    稳定性高，一个进程崩溃了，不会影响其他进程缺点:
· 缺点:
    创建进程开销巨大
    操作系统能同时运行进程数目有限

"""
import os
from multiprocessing import Process
from time import sleep


def task1(s):
    while True:
        sleep(s)
        print('task1{}->'.format(name), os.getpid(), '->', os.getppid())


def task2(s):
    while True:
        sleep(s)
        print('task2')


if __name__ == '__main__':
    # 以下是子进程
    # 创建进程对象
    p1 = Process(target=task1, name='task1', args=(1, ))
    p1.start()
    # print(p1.pid, p1.name)
    p2 = Process(target=task2, name='task2', args=(2, ))
    p2.start()

    # 以下是主进程
    print('主进程')
