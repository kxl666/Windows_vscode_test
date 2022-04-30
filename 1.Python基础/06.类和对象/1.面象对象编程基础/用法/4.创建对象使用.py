# 01可以在创建对象后定义类中不存在的属性


class Car01:

    def move(self):
        print('汽车在移动')

    def stop(self):
        print('汽车停止')


car1 = Car01()
car1.color = 'red'
car1.move()
print(car1.color)

# 02可以直接获取类的外部属性,不需要实例化 但init中的属性不能直接获取,除非实例化


class Car02:

    wheel = 4  # 这属于类属性

    def __init__(self):
        self.color = 'red'


print(Car02.wheel)
print(Car02.color)  # AttributeError: 'Car02' object has no attribute 'color'
