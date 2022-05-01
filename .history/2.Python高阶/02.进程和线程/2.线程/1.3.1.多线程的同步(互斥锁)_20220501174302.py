# 在一个进程内的所有线程共享全局变量，能够在不适用其他方式的前提下完成多线程之间的数据共享（这点要比多进程要好）
# 而局部变量等是各自线程的，是非共享的，不能被其他线程访问
# 缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）

import random
import threading
import time

lock = threading.Lock()

list = [0] * 10


def task():
    lock.acquire()
    for i in range(len(list)):
        list[i] = 1
        time.sleep(random.random())
