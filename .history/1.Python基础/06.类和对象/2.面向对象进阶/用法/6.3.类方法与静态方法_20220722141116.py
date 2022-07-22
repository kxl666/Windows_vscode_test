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
        name = re.search(r'名字:(.*?), ', content).group(1)
        age = re.search(r'年龄:(\d+) ', content).group(1)
        return cls(name, age)  # 创建一个类的实例

    @classmethod
    def from_english_string(cls, content):
        name = re.search(r'name:(.*?),', content).group(1)
        age = re.search(r'age:(\d+)', content).group(1)
        return cls(name, age)  # 创建一个类的实例

    def calc_age_after_year(self, year):
        age = People.add_two_number(self.age, year)
        print(f'{year}年之后的年龄是{age}')


content = 'my name:张三, my age:18'
people = People.from_english_string(content)
people.introduce_myself()
people.calc_age_after_year(10)
