# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
# 不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print(
        'Hello, %s (in %s)' %
        (std, threading.current_thread().name))  # current_thread().name 是线程名称


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread,
                      args=('dongGe', ),
                      name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('老王', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
