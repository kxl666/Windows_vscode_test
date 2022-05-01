# 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()
import os
import time
from multiprocessing import Manager, Pool


def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        time.sleep(0.3)
        print("reader从Queue获取到消息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "dongGe":
        time.sleep(0.2)
        q.put(i)
        print("writer向Queue中写入消息：%s" % i)


if __name__ == "__main__":
    print("(%s) start" % os.getpid())

    q = Manager().Queue()  # 使用Manager中的Queue来初始化
    po = Pool()
    # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    po.apply(writer, (q, ))
    po.apply(reader, (q, ))
    po.close()  # 关闭进程池，不再接受新的进程
    po.join()  # 等待po中的所有子进程执行完成

    print("(%s) End" % os.getpid())
