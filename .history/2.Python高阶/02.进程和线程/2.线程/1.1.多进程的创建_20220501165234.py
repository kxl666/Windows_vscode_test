from threading import Thread
from time import sleep


def download(n):
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for image in images:
        print('正在下载：', image)
        sleep(n)
        print('{}下载完成：'.format(image))


if __name__ == '__main__':
    t = Thread(target=download, args=(1, ))
    t.start()

    n = 1
    while True:
      