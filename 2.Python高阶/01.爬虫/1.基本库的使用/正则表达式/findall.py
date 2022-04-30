# 多个匹配模式，返回元组列表：
import re

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

# 结果：
# ['width=20', 'height=10']
