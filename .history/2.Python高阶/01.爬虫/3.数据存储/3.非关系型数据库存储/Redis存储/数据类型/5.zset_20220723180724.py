from redis_default import con

con.zadd('test', 'apple', 1, 'a', 2, 'b', 3, 'c')  # 向集合中添加元素
