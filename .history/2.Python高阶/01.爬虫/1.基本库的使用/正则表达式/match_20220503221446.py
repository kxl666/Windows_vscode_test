# 01 group()
# 02 编译标志
"""
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print(matchObj)
if matchObj:
    print("matchObj.groups() : ", matchObj.groups())  # 返回一个包含所有小组字符串的 元组
    print("matchObj.group() : ", matchObj.group())  # 返回一个 匹配的字符串
    print("matchObj.group(1) : ", matchObj.group(1))  # 返回第一个小组字符串
    print("matchObj.group(2) : ", matchObj.group(2))  # 返回第二个小组字符串
else:
    print("No match!!")
