import time

import gevent
from gevent import monkey

monkey.patch_all()
# 猴子补丁，把程序中的time.sleep()换成gevent.sleep()
'''
gevent是类似一个协程空间，当你用生成协程时，就会在gevent容器空间中生成一个标记好的协程，
当多个协程同时存储在容器空间时，gevent就会统一调配CPU的使用，当那个协程出现堵塞时，
gevent就会马上切换执行到下一个协程标记中去，实现一个非堵塞的运行gevent容器空间！

'''


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
