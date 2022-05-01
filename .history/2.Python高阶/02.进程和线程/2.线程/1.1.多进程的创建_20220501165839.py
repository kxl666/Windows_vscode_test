from threading import Thread
from time import sleep


def download(n):
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for image in images:
        print('正在下载：', image)
        sleep(n)
        print('{}下载完成：'.format(image))


def listenMusic(n):
    musics = ['1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3']
    for music in musics:
        print('正在播放：', music)
        sleep(n)
        print('{}播放完成：'.format(music))


if __name__ == '__main__':
    t1 = Thread(target=download, args=(1, ))
    t1.start()
    # t1.join()

    t2 = Thread(target=listenMusic, args=(1, ))
    t2.start()
    # t1等待的时候,cpu会执行t2,t2等待的时候,cpu会执行t1, 因此t1和t2是并行的
    # t2.join()
    # 主线程
    # n = 1
    # while True:
    #     print(n)
    #     sleep(1.2)
    #     n += 1
