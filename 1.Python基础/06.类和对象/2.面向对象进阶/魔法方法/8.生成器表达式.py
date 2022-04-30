# 列表推导式
list1 = [i for i in range(100) if not (i % 2) and i % 3]
print(list1)

# 字典推导式
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}  #
print(stocks2)

# 元组推导式,没有字符串推导式
tuple1 = (i for i in range(6))
print(tuple1)  # <generator object <genexpr> at 0x000001E9D8B8B848> # 生成器表达式
print(next(tuple1))
print(next(tuple1))
print(next(tuple1))

# 用法 将生成器表达式作为函数的参数使用
print(sum(i for i in range(10) if not (i % 2)))
