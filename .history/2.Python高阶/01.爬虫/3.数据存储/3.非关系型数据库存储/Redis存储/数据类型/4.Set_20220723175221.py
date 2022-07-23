from redis_default import con

con.sadd('Zarten', 'apple', 'a', 'b', 'c', 'c') # 向集合中添加元素
print(con.smembers('Zarten')) # 获取集合中的所有元素
