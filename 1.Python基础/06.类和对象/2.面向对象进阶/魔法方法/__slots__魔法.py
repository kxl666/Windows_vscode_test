# 实例的dict只保持实例的变量，对于类的属性是不保存的，类的属性包括变量和函数。
# 由于每次实例化一个类都要分配一个新的dict，因此存在空间的浪费，因此有了__slots__。
# __slots__是一个元组，包括了当前能访问到的属性。
# 当定义了slots后，slots中定义的变量变成了类的描述符，相当于java，c++中的成员变量声明，
# 类的实例只能拥有slots中定义的变量，不能再增加新的变量。注意：定义了slots后，就不再有dict


class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 15)
    person.play()
    # person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
