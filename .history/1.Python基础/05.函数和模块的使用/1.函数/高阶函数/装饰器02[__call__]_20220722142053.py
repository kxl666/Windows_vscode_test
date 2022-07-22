import random
import time
from functools import wraps

# 类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式


class RecordTime:

    def __call__(self, func):
        # 如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象
        # 实例对象也可以像函数一样作为可调用对象来用，那么，这个特点在什么场景用得上呢？
        # 这个要结合类的特性来说，类可以记录数据（属性），而函数不行（闭包某种意义上也可行），利用这种特性可以实现基于类的装饰器，在类里面记录状态

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("%s执行时间:%.2f" % (func.__name__, end - start))
            return result

        return wrapper


# 使用装饰器语法糖添加装饰器
@RecordTime()
def download(filename):
    print("开始下载", filename)
    time.sleep(random.randint(2, 6))
    print(filename, "下载完成")


def upload(filename):
    print("开始上传", filename)
    time.sleep(random.randint(4, 8))
    print(filename, "上传完成.")


# 直接创建对象并调用对象传入被装饰的函数
upload = RecordTime()(upload)  # 用法
download = RecordTime()(download)
download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')
