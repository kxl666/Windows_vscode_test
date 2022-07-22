# 定义一个类
class Animal:

    def __init__(self, name):
        self.name = name

    def printName(self):
        print(f"名字为：{self.name}")


# 定义一个函数,传入一个对象
# 内部调用


def myPrint(animal):
    animal.printName()


dog1 = Animal("小狗")
myPrint(dog1)

dog2 = Animal("小猫")
myPrint(dog2)
