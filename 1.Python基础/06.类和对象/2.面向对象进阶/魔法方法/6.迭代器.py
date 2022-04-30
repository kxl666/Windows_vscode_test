# 迭代输出生成器的内容
# 生成器是生成元素的，迭代器是访问集合元素的一中方式

# 迭代的意思类似循环
# 可迭代对象 Iterable(列表,元组,字符串),字典等
# 迭代器 Iterator(可以访问迭代器中的每一个元素)

# 可以使用 isinstance() 判断一个对象是否是 Iterable 对象
# 可以使用isinstance()判断一个对象是否是Iterator对象
# # 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

# 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 凡是可作用于 next() 函数的对象都是 Iterator 类型
# 集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象

# 01 通常使用for语句来进行迭代:
for i in "FishC":
    print(i)

# 02 字典与文件也支持迭代
links = {"柯小乐": "01", "柯鑫": "02", "柯大爷": "03"}

for each in links:
    print(each)

# 03 BIF-> iter(),next()
string = "FishC"
it = iter(string)  # 将字符串转换为迭代器，从而使next()函数可以不断获取下一个值
print(next(it))
print(next(it))

# 04 魔法方法 __iter__(),__next__()
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在StopIteration的value中

# 迭代器需要我们去定义一个类和实现相关的方法,而生成器只需要在普通的函数中加上一个yield关键字就可以了


class Fibs:

    def __init__(self, n=20):
        self.a = 1
        self.b = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


# fibs=Fibs()
fibs = Fibs(10)
for each in fibs:
    print(each)
