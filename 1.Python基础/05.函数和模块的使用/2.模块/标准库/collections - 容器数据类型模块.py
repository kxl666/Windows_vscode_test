# 01 namedtuple
# 命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类
from collections import Counter, OrderedDict, namedtuple

Card = namedtuple('Card', ('suite', 'face'))
card1 = Card('红桃', 5)
card2 = Card('草花', 9)
print(card1)
print(card2.suite, card2.face)
print(card2._fields)  # 显示字段名
card2 = card2._replace(face=10)  # 修改对象属性_此时无法直接修改对象中是属性,因为默认是元组
print(card2)
card3 = Card._make(['方块', 13])  # 通过一个list来创建一个User对象
print(card3)
print(card3._asdict())

# 02 Counter
# dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。
# Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
    'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
    'under'
]
counter = Counter(words)
# 打印words列表中出现频率最高的3个元素及其出现次数-most_common
for elem, count in counter.most_common(3):
    print(elem, count)  # 元组
print(counter.most_common(3))  # 字典

# 统计词频-dict
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(dict(c))

# 获得所有元素-elements
c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

# Counter更新_普通字典是不支持拼接和重复操作的
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)  # 相加
# Counter({'a': 4, 'b': 3})
print(c - d)  # 相减，如果小于等于0，删去
# Counter({'a': 2})
print(c & d)  # 求最小
# Counter({'a': 1, 'b': 1})
print(c | d)  # 求最大
# Counter({'a': 3, 'b': 2})
print(c['a'])

# 【例子】
# 读文件统计词频并按照出现次数排序，文件是以空格隔开的单词的诸多句子
lines = open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
             "r").read().splitlines()  #
lines = [lines[i].split(" ") for i in range(len(lines))]  # 列表推导式
words = []
for line in lines:
    words.extend(line)
result = Counter(words)
print(result.most_common(10))

# 当需要统计的文件比较大，使用read()一次读不完的情况

result = Counter()
with open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
          "r") as f:
    while True:
        lines = f.read(1024).splitlines()
        if lines == []:
            break
        lines = [lines[i].split(" ") for i in range(len(lines))]
        words = []
        for line in lines:
            words.extend(line)
        tmp = Counter(words)
        result += tmp

print(result.most_common(10))

# 03 OrderedDict
# dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为

# 定义有序字典
dic2 = OrderedDict()
dic2['a'] = '123'
dic2['b'] = 'jjj'
dic2['c'] = 'abc'
dic2['d'] = '999'
for k, v in dic2.items():
    print('有序字典：%s:%s' % (k, v))
