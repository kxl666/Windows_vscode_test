class C:

    def __getattribute__(self, name):
        print("get")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print("set")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print("del")
        super().__delattr__(name)

    def __getattr__(self, name):
        print("getattr")


c = C()
print(c.x)
c.x = 1
print(c.x)
del c.x
setattr(c, 'y', "Red")


# 实例:计算矩形面积
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == "square":
            self.width = value
            self.height = value
        else:
            super().__setattr__(name, value)

    def getArea(self):
        return self.width * self.height


r1 = Rectangle(4, 5)
print(r1.getArea())
r1.square = 10
print(r1.getArea())
