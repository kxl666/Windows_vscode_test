import random
import time
from functools import wraps


def record_time(func):

    @wraps(
        func
    )  # 这个装饰器可以帮我们保留被装饰之前的函数，这样在需要取消装饰器时，可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)  # result = func(*args, **kwargs) 没区别
        end = time.time()
        print("%s执行时间:%.2f" %
              (func.__name__, end - start))  # func.__name__ 是被装饰的函数的名字
        # return result

    return wrapper


@record_time
def download(filename):
    print("开始下载", filename)
    time.sleep(random.randint(2, 6))
    print(filename, "下载完成")


@record_time
def upload(filename):
    print("开始上传", filename)
    time.sleep(random.randint(4, 8))
    print(filename, "上传完成.")


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

# 取消装饰器
download.__wrapped__('MySQL必知必会.pdf')
upload = upload.__wrapped__
upload('Python从新手到大师.pdf')
