import gevent


def a():
    for i in range(5):
        print('A' + str(i))
        gevent.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        gevent.sleep(0.1)


def c():
    for i in range(5):
        print('C' + str(i))
        gevent.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)
    gevent.joinall([g1, g2, g3])
    print('--------------')

# 结果实现了交替运行
