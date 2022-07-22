import re


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_myself(self):
        print("我叫%s,今年%d岁" % (self.name, self.age))

    @staticmethod
    def add_two_number(a, b):
        a_int = int(a)
        b_int = int(b)
        return a_int + b_int

    @classmethod
    def from_chinese_string(cls, content):
        name = re.search('名字：(.*?),', content).group(1)
        age = re.search('年龄：(\d+)', content).group(1)
        return cls(name, age)  # 创建一个类的实例

    @classmethod
    def from_english_string(cls, content):
        name = re.search('name:(.*?),', content).group(1)
        age = re.search('age:(\d+)', content).group(1)
        return cls(name, age)  # 创建一个类的实例

    def calc_age_after_year(self, year):
        age = People.add_two_number(self.age, year)
        print("我今年%d岁,%d年后我将会是%d岁" % (self.age, year, age))


content = 'my name: is 张三, my age:I am 18 years old.'
people = People.from_english_string(content)
people.introduce_myself()
people.calc_age_after_year(10)
