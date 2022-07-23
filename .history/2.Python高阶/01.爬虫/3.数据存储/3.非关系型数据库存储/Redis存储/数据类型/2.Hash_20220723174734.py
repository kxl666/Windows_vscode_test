from redis_default import con

con.hset('user', 'name', 'kx')  # 存储hash类型数据
con.hset('user', 'age', '18')

print(con.hget('user', 'name'))  # 获取hash类型数据
print(con.hmget('user', 'name', 'age'))  # 获取多个hash类型数据
con.delete('user')  # 删除hash类型数据

con.hmset('user2', {
    'name': 'kx',
    'age': '18',
    'score': 100,
    'money': 12.5
})  # 存储多个hash类型数据
print(con.hgetall('user2'))  # 获取所有hash类型数据

print(con.hlen('user2'))  # 获取hash类型数据的长度
print(con.hkeys('user2'))  # 获取hash类型数据的所有key
print(con.hvals('user2'))  # 获取hash类型数据的所有value

con.hdel('user2', 'name')  # 删除hash类型数据中的某个key
print(con.hgetall('user2'))

con.hincrby('user2', 'score', 10)  # 对hash类型数据中的某个key的value值进行加10操作
con.hincrbyfloat('user2', 'money', 0.5)  # 对hash类型数据中的某个key的value值进行加0.5操作
print(con.hgetall('user2'))

print(con.hscan('user2'))  # 获取hash类型数据中的某个key的value值
