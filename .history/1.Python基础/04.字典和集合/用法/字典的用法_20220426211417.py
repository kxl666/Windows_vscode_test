# 01

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


# 2
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)  # 解包

# 3只会输出键
links = {"柯小乐": "01", "柯鑫": "02", "柯大爷": "03"}

for each in links:
    print(each)  # 可以print(links[each])输出值

for keys in links.keys():
    print(keys)

# 4输出值

for values in links.values():
    print(values)

# 5输出键值对
for key, value in links.items():
    print(key, value)

# 6字典的键只能是不可变类型
