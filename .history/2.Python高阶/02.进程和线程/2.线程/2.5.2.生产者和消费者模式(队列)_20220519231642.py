import threading
import time
from queue import Queue


class Producer(threading.Thread):

    def run(self):
        global queue
        count = 0
        while queue.qsize() <= 20:
            for _ in range(10):
                count = count + 1
                msg = f'生成产品{str(count)}'
                queue.put(msg)
                print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):

    def run(self):
        global queue
        while queue.qsize() >= 10:
            for _ in range(3):
                msg = f'{self.name} 消费了 {queue.get()}'
                print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()

    for i in range(10):
        queue.put(f'初始产品{str(i)}')
    for _ in range(2):
        p = Producer()
        p.start()
    for _ in range(5):
        c = Consumer()
        c.start()
