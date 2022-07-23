from redis_default import con

con.zadd('test', {'a', 1, 'b', 2, 'c', 3})  # 向集合中添加元素
