from redis_default import con

con.zadd('Zarten', 'apple', 1, 'a', 2, 'b', 3, 'c')  # 向集合中添加元素
print(con.zrange('Zarten', 0, -1, withscores=True))  # 获取集合中的所有元素