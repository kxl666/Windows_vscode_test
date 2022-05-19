# 生产者与消费者：两个线程之间的通信方式，一个线程生产数据，另一个线程消费数据
import queue
import random
import threading
import time


def produce(q):
    for _ in range(10):
        num = random.randint(1, 100)
        q.put('生产者产生数据：%d' % num)
        print('生产者产生数据：%d \n' % num)
        time.sleep(1)
    q.put(None)  # 发送结束信号
    q.task_done()  # 告诉队列，生产者结束


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'消费者消费--->{item}')
        time.sleep(1)
    q.task_done()  # 告诉队列，生产者结束,在一对一的生产者与消费者中起作用


if __name__ == '__main__':
    q = queue.Queue(10)  # 初始化队列，最多可以存放10个数据
    t1 = threading.Thread(target=produce, args=(q, ))
    t1.start()
    t2 = threading.Thread(target=consume, args=(q, ))
    t2.start()

    t1.join()
    t2.join()
