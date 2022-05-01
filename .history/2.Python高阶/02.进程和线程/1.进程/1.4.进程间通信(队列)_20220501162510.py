from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['1.jpg', '2.jpg', '3.jpg']
    for image in images:
        print('downloading %s' % image)
        sleep(0.5)
        q.put(image)


def getFile():



if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getFile, args=(q,))
