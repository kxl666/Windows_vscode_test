a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = (1, 2, 3)
print(a, b, c)
a, b, c = [1, 2, 3]
print(a, b, c)
a, b, c = (1, 2, 3, 4)
print(a, b, c)  # 报错
a, b, c = [1, 2, 3, 4]
print(a, b, c)  # 报错

# 1.添加
# 1.1 append() 在列表末尾添加新的对象
# 1.2 extend() 在列表末尾一次性追加另一个序列中的多个值
# 1.3 insert() 在指定位置插入一个新的对象
