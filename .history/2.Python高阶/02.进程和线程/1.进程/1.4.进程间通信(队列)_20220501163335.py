from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['1.jpg', '2.jpg', '3.jpg']
    for image in images:
        print('downloading %s' % image)
        sleep(0.5)
        q.put(image)


def getFile(q):
    while True:
        # 第一种判断队列是否为空的方法
        # try:
        #     image = q.get(timeout=3)  # 从队列中获取数据，超时3秒后报错
        #     print('download %s success' % image)
        # except Exception as e:
        #     print(e)
        #     break

        # 第二种判断队列是否为空的方法
        if not q.empty():
            image = q.get()
            print('download %s success' % image)
        else:
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q, ))
    p2 = Process(target=getFile, args=(q, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('main process end')
