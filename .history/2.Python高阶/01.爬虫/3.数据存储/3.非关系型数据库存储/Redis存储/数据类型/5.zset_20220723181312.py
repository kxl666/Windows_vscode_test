from redis_default import con

con.zadd('test', {'a': 3, 'b': 2, 'c': 1})  # 向集合中添加元素
print(con.zrange('test', 0, -1))  # 获取集合中的元素和分数
