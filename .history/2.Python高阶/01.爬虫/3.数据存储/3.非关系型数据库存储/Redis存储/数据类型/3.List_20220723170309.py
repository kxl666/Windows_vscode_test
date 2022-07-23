from redis_default import con

con.lpush('num', '1', 2, 'kx', 1.2)  # 存储列表
