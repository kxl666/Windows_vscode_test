# p2_1.py
def num(n=101, i=2):
    # i=2
    while n < 200:
        while i < n / 2:
            if n % i == 0:
                continue
            i += 1
        if i > n / 2:
            print(n)
        n += 1


num(n=103, i=2)

# 一行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(
    map(lambda f: x % f, range(2,
                               int(x**0.5) + 1)))
# 用法

print(is_prime(7))
