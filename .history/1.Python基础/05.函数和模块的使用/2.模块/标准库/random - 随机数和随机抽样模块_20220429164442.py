import random

# 产生 0 到 1 之间的随机浮点数-random
print(random.random())

# 产生 1 到 10 的一个整数型随机数-randint
print(random.randint(1, 10))

# 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数-uniform
print(random.uniform(1.1, 5.4))

# 从序列中随机选取一个元素-choice
print(random.choice('tomorrow'))

#

# 生成从1到100的间隔为2的随机整数-randrange
print(random.randrange(1, 100, 2))

# 将序列a中的元素顺序打乱-shuffle
a = [1, 3, 5, 6, 7]
random.shuffle(a)
print(a)

# 多个字符中生成指定数量的随机字符,用于无重复的随机抽样a用于无重复的随机抽-sample
print(random.sample("zyxwvutsrqponmlkjihgfedcba", 5))
