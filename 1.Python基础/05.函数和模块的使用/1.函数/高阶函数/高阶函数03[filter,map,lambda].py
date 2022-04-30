# 01
def is_even(num):
    return (num % 2 == 0)


def square(num):
    return (num**2)


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))  #
print(numbers2)  # [144, 64, 3600, 2704]

# 02生成式
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = [num**2 for num in numbers1 if num % 2 == 0]  # 更加简洁
print(numbers2)  # [144, 64, 3600, 2704]

# 03匿名函数
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers1)))  #
print(numbers2)  # [144, 64, 3600, 2704]
