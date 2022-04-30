# property 事实上就是一个描述符类


class MyProperty:

    def __init__(self, Get=None, Set=None, Del=None):
        self.Get = Get
        self.Set = Set
        self.Del = Del

    def __get__(self, instance, owner):
        return self.Get(instance)

    def __set__(self, instance, value):
        self.Set(instance, value)

    def __delete__(self, instance):
        self.Del(instance)


class C:

    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


c = C()
c.x = "kxl666"
print(c.x)

# del c.x
# print(c.x)


# 实例: 给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果。
class Celsius:

    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:

    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 3.2

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


temp = Temperature()
print(temp.cel)
temp.fah = 100
print(temp.cel)
