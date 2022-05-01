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
from multiprocessing import Process
from time import sleep


def task1():
    while True:
        sleep(1)
        print('task1')


def task2():
    while True:
        sleep(1)
        print('task2')


def main():
    p1 = Process(target=task1)
    p2 = Process(target=task2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
