# 定制容器
# 编写一个不可改变的自定义列表,记录访问每个元素的次数
class countList:

    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]


c1 = countList(1, 3, 5, 7, 9)
c2 = countList(2, 4, 6, 8)
print(c1[1])
print(c1.count)
print(c2[1])
print(c2.count)
