# python3中有两种方式控制对象转字符串，第一种就是__str__,第二种就是__repr__,两种的工作方式大体相同，只是调用的时机不同
# 当直接查看对象的时候调用的是__repr__方法，对象需要转字符串的时候调用的是__str__方法，但是当字典列表等容器的时候调用的还是__repr__方法
import datetime


class T:

    def __repr__(self):
        return self.color + "__str__"

    def __init__(self):
        self.color = "red"
        self.count = 2


t = T()
print(t)

# __str__ 和 __repr__ 的差别

today = datetime.datetime.now()
print(today)
print(repr(today))
# __str__的可读性更强，而__repr__的返回结果更具有准确性，更加的适合开发者
