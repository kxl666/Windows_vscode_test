from multiprocessing import Process, Queue
from time import sleep

def download():
    images = ['1.jpg', '2.jpg', '3.jpg']
    for image in images:
        print('downloading %s' % image)
        sleep(0.5)


def getFile():
    