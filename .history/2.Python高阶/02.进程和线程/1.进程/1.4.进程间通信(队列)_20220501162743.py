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
        image = q.get(timeout=3)
        print('download %s success' % image)


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q, ))
    p2 = Process(target=getFile, args=(q, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('main process end')
