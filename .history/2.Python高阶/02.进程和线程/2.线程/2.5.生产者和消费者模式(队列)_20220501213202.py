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
        print('生产者产生数据：%d \n' % num)
        time.sleep(1)
        i += 1

    q.put(None)  # 发送结束信号
    # q.task_done()  # 告诉队列，生产者结束


def consume(q):
    while True:
        if not q.empty():
            item = q.get()
            print('消费者消费--->%s' % item)
        else:
            break
        time.sleep(1)
    # q.task_done()  # 告诉队列，生产者结束


if __name__ == '__main__':
    q = queue.Queue(10)  # 初始化队列，最多可以存放10个数据
    # t1 = threading.Thread(target=produce, args=(q, ))
    # t1.start()
    # t2 = threading.Thread(target=consume, args=(q, ))
    # t2.start()

    # t1.join()
    # t2.join()

    for _ in range(2):
        p = threading.Thread(target=produce, args=(q, ))
        p.start()

    for _ in range(3):
        c = threading.Thread(target=consume, args=(q, ))
        c.start()
    # print('main process end')
