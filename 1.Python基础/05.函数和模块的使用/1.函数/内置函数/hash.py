# hash的参数只能是不可变类型，如字符串，整数，元组，None等,不能是列表，字典，集合等
# 作用：计算对象的哈希值，用于字典的键值对的比较
print(hash(1))
print(hash(1.0))
print(hash('1'))

print(hash([1, 2]))  # 列表或字典会报错
