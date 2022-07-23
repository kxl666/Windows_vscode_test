from redis_default import con

con.zadd('test', {'a': 3, 'b': 2, 'c': 1})  # 向集合中添加元素
print(con.zrange('test', 0, -1))  # 获取集合中的元素
print(con.zrange('test', 0, -1, withscores=True))  # 获取集合中的元素
print(con.zrevrange('test', 0, -1))  # 获取集合中的元素，从大到小排列
print(con.zrangebyscore('test', 0, 10))  # 获取集合中指定分数范围内的元素

print(con.zscore('test', 'a'))  # 获取集合中指定元素的分数
print(con.zcard('test'))  # 获取集合中元素的数量
print(con.zcount('test', 0, 10))  # 获取集合中指定分数范围内的元素数量

con.zincrby('test', 'a', 2)  # 对集合中指定元素的分数加上指定值
print(con.zscore('test', 'a'))

con.zrem('test', 'a')  # 删除集合中指定元素
print(con.zrange('test', 0, -1))
