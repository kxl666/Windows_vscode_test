# greenlet已经实现了协程，但是这个还要人工切换，这里介绍一个比greenlet更强大而且能够自动切换任务的第三方库，那就是gevent。
from time import time

import gevent


def a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


def c():
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.1)
