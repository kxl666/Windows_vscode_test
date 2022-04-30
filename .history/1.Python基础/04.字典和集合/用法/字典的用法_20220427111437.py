# 01 获取元素

students = {
    1001: {
        'name': '狄仁杰',
        'sex': True,
        'age': 22,
        'place': '山西大同'
    },
    1002: {
        'name': '白元芳',
        'sex': True,
        'age': 23,
        'place': '河北保定'
    },
    1003: {
        'name': '武则天',
        'sex': False,
        'age': 20,
        'place': '四川广元'
    }
}

print(students.get(
    1002))  # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(students.get(1005))  # None
print(students.get(1005, {'name': '无名氏'}))  # {'name': '无名氏'}
print(students[1001]['name'])


# 2 不定长参数
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)  # 解包

# 3.只会输出键
links = {"柯小乐": "01", "柯鑫": "02", "柯大爷": "03"}

for each in links:
    print(each)  # 可以print(links[each])输出值

for keys in links.keys():
    print(keys)

# 4.输出值

for values in links.values():
    print(values)

# 5.输出键值对
for key, value in links.items():
    print(key, value)

# 6.字典的键只能是不可变类型,字典的值可以是任何类型

# 7.删除
# 7.1 pop() 删除列表中的一个元素,参数为索引值,默认删除最后一个元素
# 7.2 popitem() 删除字典中的一个键值对,默认删除最后一个键值对
# 7.3 del 删除整个字典,也可以删除指定的键值对
# 7.4 clear() 清空字典

# 8.更新
# 8.1 update() 更新字典,参数为字典或dict.update(key=value)
# 8.2 setdefault() 如果键不存在,则添加键值对,如果键存在,则不添加
# 8.3 fromkeys() 创建一个新字典,参数为序列,默认值为None
# 8.4 copy() 浅拷贝
