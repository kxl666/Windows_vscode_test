# String类型既可以保存普通文字，也可以保存序列化的二进制数据
# String类型最大可以存储512M数据
from redis_default import con

con.set('name', '张三')  # 存储字符串
print(con.get('name'))  # 获取字符串
con.set('name', b'\x61\x62\x63')  # 存储二进制数据
