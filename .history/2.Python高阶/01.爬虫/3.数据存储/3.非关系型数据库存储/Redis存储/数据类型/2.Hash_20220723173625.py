from redis_default import con

# con.hset('user', 'name', 'kx')  # 存储hash类型数据
# con.hset('user', 'age', '18')

# print(con.hget('user', 'name'))  # 获取hash类型数据
# print(con.hmget('user', 'name', 'age'))  # 获取多个hash类型数据

con.hmset('user', {'name': 'kx', 'age': '18', 'score': 100})  # 存储多个hash类型数据
print(con.hgetall('user'))  # 获取所有hash类型数据
