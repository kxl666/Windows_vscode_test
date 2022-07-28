# greenlet已经实现了协程，但是这个还要人工切换，这里介绍一个比greenlet更强大而且能够自动切换任务的第三方库，那就是gevent。
'''
gevent是类似一个协程空间，当你用生成协程时，就会在gevent容器空间中生成一个标记好的协程，
当多个协程同时存储在容器空间时，gevent就会统一调配CPU的使用，当那个协程出现堵塞时，
gevent就会马上切换执行到下一个协程标记中去，实现一个非堵塞的运行gevent容器空间！

'''
import time

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


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)
    gevent.joinall([g1, g2, g3])
    print('--------------')

# 结果并没有交替运行
# 说明函数内部的time.sleep()不会影响主线程的运行，因为主线程的执行是由协程来控制的。
# 需要用到gevent.sleep()来控制协程的运行时间。或者monkey.patch_all()
