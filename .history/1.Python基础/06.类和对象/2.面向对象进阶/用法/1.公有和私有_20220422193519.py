# 01 变量名前面加上"__"两个下划线,就会成为私有
# 一个_名的变量、函数、类在使用from xxx import *时都不会被导入
class Person:
    __name = "柯小乐"


p = Person()

# print(p.__name)
# 无法访问


# 02
class Animal:

    def __init__(self):
        self.__name = "柯鑫"  # 私有属性

    def getName(self):
        return '%s' % self.__name

    def __getName2(self):  # 私有方法
        return '%s' % self.__name


p2 = Animal()
# 但是可以从内部访问
print(p2.getName())  # 柯鑫
print(p2.__getName2())  # 报错
# Python私有机制是伪私有,类对权限没有控制
print(p2._Animal__name)

# 1.子类对象不能在自己的方法内部。直接访问父类的私有属性或私有方法
# 2.子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
# 3.私有属性、方法通常用于做一些内部的事情
