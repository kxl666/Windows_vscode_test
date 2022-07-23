# String类型既可以保存普通文字，也可以保存序列化的二进制数据
# String类型最大可以存储512M数据
from redis_default import con

con.set('name', '张三')  # 存储字符串
print(con.get('name'))  # 获取字符串
# print(con.get('name').decode('utf-8'))  # 获取字符串
print(con.get('name', encoding='utf-8'))  # 获取字符串，指定编码
# con.set('name', b'\x61\x62\x63')  # 存储二进制数据
con.mset({'name': '张三', 'age': '18'})  # 存储多个键值对
print(con.mget('name', 'age'))  # 获取多个键值对
print(con.getrange('age', 0, 3))  # 获取字符串的一部分
print(con.)