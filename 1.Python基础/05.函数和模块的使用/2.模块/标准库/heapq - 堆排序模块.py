import heapq
from pprint import pprint

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# 找出列表中最大的三个元素
# print(heapq.nlargest(3, list1))
# 找出列表中最小的1个元素
# print(heapq.nsmallest(1, list1))
# print(min(list1))
# 找出列表中第一个值
# print(heapq.heappop(list1))

list2 = [{
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}, {
    'name': 'AAPL',
    'shares': 50,
    'price': 543.22
}, {
    'name': 'FB',
    'shares': 200,
    'price': 21.09
}, {
    'name': 'HPQ',
    'shares': 35,
    'price': 31.75
}, {
    'name': 'YHOO',
    'shares': 45,
    'price': 16.35
}, {
    'name': 'ACME',
    'shares': 75,
    'price': 115.65
}]
# 找出价格最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['price']))

pprint(heapq.nlargest(3, list2, key=lambda x: x['price']))

# 找出持有数量最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['shares']))

# 加入堆
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)
# 获取最小值
print(heap[0])
# 堆排序结果
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])

# 用于合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器
num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

res = heapq.merge(num1, num2)
print(list(res))
