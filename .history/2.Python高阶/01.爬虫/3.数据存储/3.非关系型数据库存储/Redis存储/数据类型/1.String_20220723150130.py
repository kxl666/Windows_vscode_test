# String类型既可以保存普通文字，也可以保存序列化的二进制数据
# String类型最大可以存储512M数据
import redis

con = redis.Redis(host='45.43.61.98',
                  port=6379,
                  password='Hbxs@tpp@123!@#',
                  db=0)

con.set('name', '张三')
name = con.get('name')
print(name)
