# -*- coding:utf-8 -*-

infor = [{
    "name": "kxl",
    "age": 11,
    "num": 101
}, {
    "name": "kxx",
    "age": 12,
    "num": 102
}]
print("\t*  【初始学生信息】   *")
for i in range(len(infor)):
    print("\t%s的年龄是%d,学号是%d" %
          (infor[i]["name"], infor[i]["age"], infor[i]["num"]))
input("继续请按回车")

# 添加


def Add():
    name = str(input("请输入新增的姓名:"))
    age = int(input("请输入新增的年龄:"))
    num = int(input("请输入新增的学号:"))
    add_infor = {"name": name, "age": age, "num": num}
    infor.append(add_infor)


# 删除


def Del():
    name = str(input("请输入待删除的名字:"))
    for i in range(len(infor)):
        if infor[i]["name"] == name:
            del infor[i]


# 修改


def Alter():
    name = str(input("请输入待修改的名字:"))
    for i in range(len(infor)):
        if infor[i]["name"] == name:
            infor[i]["name"] = str(input("请输入替换的名字:"))
            infor[i]["age"] = int(input("请输入替换的年龄:"))
            infor[i]["num"] = int(input("请输入替换的学号:"))


# 查询


def Find():
    name = str(input("请输入待查询的名字:"))
    for i in range(len(infor)):
        if infor[i]["name"] == name:
            print(infor[i]["name"], "的年龄是:", infor[i]["age"], "学号是:",
                  infor[i]["num"])


# 总览


def now_total():
    print("\t*  【实时学生信息】   *")
    for i in range(len(infor)):
        print("\t%s的年龄是%d,学号是%d" %
              (infor[i]["name"], infor[i]["age"], infor[i]["num"]))


# 菜单栏

while True:
    print('''
    ################################
    #           菜单栏             #
    #    添加               1      #
    #    删除               2      #
    #    修改               3      #
    #    查询               4      #
    #    退出               5      #
    #    总览               6      #
    ################################
    ''')
    choice = int(input("请输入你的选择:"))

    while choice < 1 or choice > 6:
        choice = int(input("请输入你的选择:"))
    if choice == 1:
        Add()
    elif choice == 2:
        Del()
    elif choice == 3:
        Alter()
    elif choice == 4:
        Find()
    elif choice == 5:
        break
    else:
        now_total()
        input("继续请按回车")
