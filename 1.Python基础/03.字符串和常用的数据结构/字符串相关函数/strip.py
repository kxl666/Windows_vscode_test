# 用于移除字符串 头尾 指定的字符（默认为空格或换行符）或字符序列

str = "00000003210Runoob01230000000"
print(str.strip('0'))

str2 = "   Runoob      "
print(str2.strip())

str3 = "Runoob:"
print(str3.strip(':'))
