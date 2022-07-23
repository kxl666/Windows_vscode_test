from redis_default import con

con.zadd('test', 'apple', 1, 'a', 2, 'b', 3, 'c')  # 向集合中添加元素
print(con.zrange('test', 0, -1))  # 获取集合中的所有元素