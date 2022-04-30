# 01 __add__,__sub__
# 使用Python默认方案
class Try_int(int):

    def __add__(self, other):
        return int.__add__(self, other)

    def __sub__(self, other):
        return int.__sub__(self, other)

    def __mul__(self, other):
        return int.__mul__(self, other)


a = Try_int(3)
b = Try_int(5)
print(a + b)


# 02 __add__,__sub__
# 自定义
class try_int(int):

    def __add__(self, other):
        return int(self) + int(other)

    def __sub__(self, other):
        return int(self) - int(other)


a = try_int(3)
b = try_int(8)
print(a - b)
