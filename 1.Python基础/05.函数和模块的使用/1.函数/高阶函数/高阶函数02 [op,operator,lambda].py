from operator import add, mul


# 01op
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))  # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))  # 120


# 02lambad
def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


# 调用calc函数，使用init_value和op的默认值
print(calc(1, 2, 3, x=4, y=5))  # 15
# 调用calc函数，通过lambda函数给op参数赋值
print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))  # 120


# 03.1 lambda
# 它们只是普通函数定义的语法糖。与嵌套函数定义一样，lambda函数可以从包含的作用域引用变量:
def make_incrementor(n):  # 用法
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))

# 03.2 lambda
# 另一个用途是传递一个小函数作为参数
stus = [{
    "name": "zhangsan",
    "age": 18
}, {
    "name": "lisi",
    "age": 19
}, {
    "name": "wangwu",
    "age": 17
}]

stus.sort(key=lambda x: x['name'])  # 用法
print(stus)
