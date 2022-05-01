# 生产者与消费者：两个线程之间的通信方式，一个线程生产数据，另一个线程消费数据
import threading
import time
import random
import queue


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据：%d' % num)
        print('生产者产生数据：%d' % num)
        time.sleep(1)
        i += 1

    q.put(None)
