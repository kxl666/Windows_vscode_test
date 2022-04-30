# 返回多个值


def divid(a, b):
    dealer = a // b
    remainder = a % b
    return dealer, remainder


sh, yu = divid(10, 3)  # 用法

print(sh, yu)
