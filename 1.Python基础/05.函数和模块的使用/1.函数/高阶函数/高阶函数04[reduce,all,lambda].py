import functools
import operator

# 一行代码定义求阶乘的函数
'''
reduce 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
'''

# 这里出现警告是新特性PEP-8 以下官方建议写成def fac(n):
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 2)

# 一行代码定义判断素数的函数
'''
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
'''

is_prime = lambda x: x > 1 and all(
    map(lambda f: x % f, range(2,
                               int(x**0.5) + 1)))

# 调用Lambda函数
print(fac(10))  # 3628800
print(is_prime(9))  # False
