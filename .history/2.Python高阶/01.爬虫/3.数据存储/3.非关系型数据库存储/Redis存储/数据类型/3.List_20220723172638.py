from redis_default import con

con.lpush('num1', '1', 2, 'kx', 1.2)  # 从左存储列表多种数据类型
print(con.lrange('num1', 0, -1))  # 获取列表中的数据切片取出

con.rpush('num2', '1', 2, 'kx', 1.2)  # 从右存储列表多种数据类型
print(con.lrange('num2', 0, -1))

print(con.llen('num1'))  # 获取列表的长度

con.linsert('num1', 'before', '1', '0')
# 在列表中插入数据,before表示在列表中的哪个元素前面插入,after表示在列表中的哪个元素后面插入,表示在1之前插入0
print(con.lrange('num1', 0, -1))

con.lset("num1", 0, -11)  # 把索引号是0的元素修改成-11
print(con.lrange('num1', 0, -1))

con.lrem('num1', 0, 'kx')  # 删除列表中第一次出现的kx
print(con.lrange('num1', 0, -1))

con.lpop('num1')  # 删除列表中的第一个元素
con.rpop('num1')  # 删除列表中的最后一个元素
print(con.lrange('num1', 0, -1))

print(con.lindex('num1', 0))  # 获取列表中索引号是0的元素

con.
con.delete('num1', 'num2')
