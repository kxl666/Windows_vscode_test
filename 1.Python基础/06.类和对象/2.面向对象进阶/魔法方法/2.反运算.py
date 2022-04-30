# 反运算优先级低于基本的算术运算
class NInt(int):

    def __radd__(self, other):
        return int.__sub__(other, self)


a = NInt(5)
b = NInt(3)
print(a + b)
# 由于a对象默认有__add__()方法,所以b的__radd__()没有执行
print
print(1 + b)
# 此时就会执行,注意顺序其中b的self是b的对象
