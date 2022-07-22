# 所谓重写，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法


class Person(object):
    """人"""

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
        print(f'{self._name}正在愉快的玩耍.')

    def watch_av(self):
        if self._age >= 18:
            print(f'{self._name}正在观看爱情动作片.')
        else:
            print(f'{self._name}只能观看《熊出没》.')


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self._grade}的{self._name}正在学习{course}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)  # 调用父类的方法
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f'{self._name}{self._title}正在讲{course}.')


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.age = 18
    stu.watch_av()
    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()
