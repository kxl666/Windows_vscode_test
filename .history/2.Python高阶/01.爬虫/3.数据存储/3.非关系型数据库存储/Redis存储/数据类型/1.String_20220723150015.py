# String类型既可以保存普通文字，也可以保存序列化的二进制数据
# String类型最大可以存储512M数据
from ..usage import con

con.set('name', '张三')
name = con.get('name')
print(name)
