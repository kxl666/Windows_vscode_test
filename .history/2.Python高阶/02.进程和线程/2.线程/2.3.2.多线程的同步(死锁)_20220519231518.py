# 避免死锁
#   1.程序设计时要尽量避免（银行家算法）
#   2.添加超时时间等

import threading
import time


class MyThread1(threading.Thread):

    def run(self):
        if mutexA.acquire():
            print(f'{self.name}----do1---up----')
            time.sleep(1)

            if mutexB.acquire():
                # if mutexB.acquire(timeout=5): # 设置超时时间来解决死锁
                print(f'{self.name}----do1---down----')
                mutexB.release()
            mutexA.release()


class MyThread2(threading.Thread):

    def run(self):
        if mutexB.acquire():
            print(f'{self.name}----do2---up----')
            time.sleep(1)
            if mutexA.acquire():
                # if mutexA.acquire(timeout=5): # 设置超时时间来解决死锁
                print(f'{self.name}----do2---down----')
                mutexA.release()
            mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
