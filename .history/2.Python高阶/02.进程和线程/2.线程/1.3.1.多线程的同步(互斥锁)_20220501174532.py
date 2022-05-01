# 在一个进程内的所有线程共享全局变量，能够在不适用其他方式的前提下完成多线程之间的数据共享（这点要比多进程要好）
# 而局部变量等是各自线程的，是非共享的，不能被其他线程访问
# 缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）

import random
import threading
import time

lock = threading.Lock()

list = [0] * 10


def task1():
    lock.acquire()  # 加锁
    for i in range(len(list)):
        print('-------->', list[i])
        time.sleep(random.random())
    lock.release()  # 解锁


def task2():
    lock.acquire()
    for i in range(len(list)):
        print(list[i])
        time.sleep(random.random())
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
