import time

import gevent
from gevent import monkey

monkey.patch_all()
# 猴子补丁，把程序中的time.sleep()换成gevent.sleep()
# monkey patch指的是在执行时动态替换一个函数的实现，这个函数的实现是由gevent来控制的。


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


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)
    gevent.joinall([g1, g2, g3])
    print('--------------')

# 结果也实现了交替运行
