from redis_default import con

con.sadd('Zarten', 'apple', 'a', 'b', 'c', 'c')  # 向集合中添加元素
print(con.smembers('Zarten'))  # 获取集合中的所有元素

print(con.scard('Zarten'))  # 获取集合中元素的个数
print(con.srandmember('Zarten', 2))  # 获取集合中的两个随机元素
print(con.sismember('Zarten', 'a'))  # 判断集合中是否存在某个元素

con.spop('Zarten')  # 删除集合中的一个随机元素
con.srem('Zarten', 'a', 'c')  # 删除集合中的某个元素
con.smove('Zarten', 'Zarten2', 'a')  # 将指定的元素从一个集合移动到另一个集合

print(con.sinter('Zarten', 'Zarten2'))  # 获取两个集合的交集
print(con.sunion('Zarten', 'Zarten2'))  # 获取两个集合的并集
print(con.sdiff('Zarten', 'Zarten2'))  # 获取两个集合的差集
print(con.sinterstore('Zarten3', 'Zarten', 'Zarten2'))  # 获取两个集合的交集并存储到指定的集合中
print(con.sunionstore('Zarten3', 'Zarten', 'Zarten2'))  # 获取两个集合的并集并存储到指定的集合中
print(con.sdiffstore('Zarten3', 'Zarten', 'Zarten2'))  # 获取两个集合的差集并存储到指定的集合中
