from redis_default import con

con.lpush('num', '1', 2, 'kx', 1.2)  # 存储列表多种数据类型
print(con.lrange('num', 0, -1))  # 获取列表中的数据
