# 一句话总结：当你想使用工厂模式，根据不同的参数生成同一个类的不同对象的时候，就可以使用类方法。
import re


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_myself(self):
        print(f'大家好：我叫{self.name}')

    @staticmethod
    def add_two_number(a, b):
        a_int = int(a)
        b_int = int(b)
        return a_int + b_int

    @classmethod
    def from_chinese_string(cls, content):
        name = re.search(r'名字:(.*?),', content)[1]
        age = re.search(r'年龄:(\d+)', content)[1]
        return cls(name, age)  # 创建一个类的实例

    @classmethod
    def from_english_string(cls, content):
        name = re.search(r'name:(.*?),', content)[1]
        age = re.search(r'age:(\d+)', content)[1]
        return cls(name, age)  # 创建一个类的实例

    def calc_age_after_year(self, year):
        age = People.add_two_number(self.age, year)
        print(f'{year}年之后的年龄是{age}')


content1 = 'my name:张三, my age:18'
people1 = People.from_english_string(content1)
people1.introduce_myself()
people1.calc_age_after_year(10)

content2 = '名字:张三, 年龄:18'
people2 = People.from_chinese_string(content2)
people2.introduce_myself()
people2.calc_age_after_year(10)
