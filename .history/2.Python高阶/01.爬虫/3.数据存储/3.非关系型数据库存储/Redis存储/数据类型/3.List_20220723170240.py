from redis_default import con

con.lpush(
    'num',
    '1',
)  # 存储列表
