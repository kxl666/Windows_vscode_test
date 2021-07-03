# p2_1.py
"""---第一个小游戏-vbvttt--"""
temp=input("不妨猜下我心里想的那个数字：")
guess=int(temp)

if guess ==8:
    print("你真棒！")
    print("猜对了！也没用！")
else:
    print("猜错了！答案是8！")
    print("游戏结束")

sum=0
for i in range(101):
    sum+=1
print(sum)