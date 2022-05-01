# 生产者与消费者：两个线程之间的通信方式，一个线程生产数据，另一个线程消费数据
import queue
import random
import threading
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据：%d' % num)
        print('生产者产生数据：%d' % num)
        time.sleep(1)
        i += 1

    q.put(None)  # 发送结束信号
    q.task_done()  # 告诉队列，生产者结束


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者消费数据：%s' % item)
        time.sleep(1)

        q.task_done()  # 告诉队列，消费者结束


if 