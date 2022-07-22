# -*- coding: utf-8 -*-


class Person(str):

    def __new__(cls, name):  # 也是一种静态方法
        print('__new__ called.')
        return str.__new__(cls, name)

    def __init__(self, name):
        print('__init__ called.')
        self.name = name

    def __str__(self):
        return '<Person: %s>' % (self.name)


if __name__ == '__main__':
    name = Person("xxx")
    print(name)
