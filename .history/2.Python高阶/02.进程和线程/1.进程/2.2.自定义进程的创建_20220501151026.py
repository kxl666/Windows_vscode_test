from multiprocessing import Process


class MyProcess(Process):

    def run(self):
        n = 1
        while True:
            print('{}--->自定义进程,n:{}'.format(self.name, n))
            n += 1


if __name__ == '__main__':
    p1 = MyProcess('小明')
    p1.start()
