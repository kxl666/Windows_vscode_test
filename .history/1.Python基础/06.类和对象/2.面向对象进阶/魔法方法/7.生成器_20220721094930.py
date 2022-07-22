# 协同程序就是可以运行的独立函数调用,函数可以暂停或者挂起#
# 生成器Generators 同样是可迭代对象，但是你只能读取一次，因为它并没有把所有值存放内存中，它动态的生成值
# yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用
# 一次 next() 就返回一个 generator 的值。
# 生成器是迭代器的一种实现


# 01
# yield 与 return 是有相似之处的，但是 yield 不会立即返回，而是将结果暂时保存起来，直到下一次调用 next() 时才返回。
def MyGen():
    print("生成器被执行！")
    for i in range(10):
        print("生成器接收到的值为：", (yield i))
    yield 1  # 结果为：1
    yield 2  # 结果为：2 没有 生成器接收到的值为：None


#
myg = MyGen()
print(next(myg))
print(next(myg))
print(myg.__next__())  # __next__() 与 next()等价
print(myg.send("hhh"))  # 与 next()等价但是 send()可以接收参数不会输出None

# # 02
for i in MyGen():
    print(i)


# 02-1 实例: 非彼拉起数列
def fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


# yield 与 return 是有相似之处的，但是 yield 不会立即返回，而是将结果暂时保存起来，直到下一次调用 next() 时才返回。

for each in fibs():
    if each > 100:
        break
    print(each)


# 02-2
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
