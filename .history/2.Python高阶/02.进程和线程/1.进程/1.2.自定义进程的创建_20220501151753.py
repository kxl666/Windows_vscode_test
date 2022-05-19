from multiprocessing import Process
from time import sleep


class MyProcess(Process):

    def __init__(self, name):  # 重写父类的__init__方法
        super().__init__()
        self.name = name

    def run(self):  # 子进程要执行的代码,重写父类的run方法
        n = 1
        while True:
            sleep(1)
            print('{}--->自定义进程,n:{}'.format(self.name, n))
            n += 1


if __name__ == '__main__':
    p1 = MyProcess('小明')
    p1.start()

    p2 = MyProcess('小红')
    p2.start()
