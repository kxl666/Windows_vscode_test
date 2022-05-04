# p2_1.py

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d " % (j, i, i * j), end='')
    print("\n")

# 打印乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')  # 用法 注意这里的f'{i}*{j}={i*j}'
    print()
