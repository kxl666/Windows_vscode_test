from abc import ABCMeta, abstractmethod


# object 为python3x 新式类
class Pet(object, metaclass=ABCMeta):  # 继承object新式类
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod  # 抽象方法不能被直接实例化, 要想使用抽象类, 必须继承该类并实现该类的所有抽象方法 # 加上abstractmethod装饰器后严格控制子类必须实现这个方法
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]  #
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
