import redis

con = redis.Redis(host='45.43.61.98',
                  port=6379,
                  password='Hbxs@tpp@123!@#',
                  db=0,
                  decode_responses=True,
                  charset='UTF-8',
                  encoding='UTF-8')
