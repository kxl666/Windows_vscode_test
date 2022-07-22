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
    def from_chinese_string(cls, chinese_string):
        name = re.findall(r"姓名:(.*?)\n", chinese_string)[0]
        age = re.findall(r"年龄:(.*?)\n", chinese_string)[0]
        return cls(name, age)

    @classmethod
    def from_english_string(cls, english_string):
        name = re.findall(r"Name:(.*?)\n", english_string)[0]
        age = re.findall(r"Age:(.*?)\n", english_string)[0]
        return cls(name, age)
    
    def calc_age_after_year(self, year):
        age = People.add_two_number(self.age, year)
        print("我今年%d岁,%d年后我将会是%d岁" % (self.age, year, age))


if __name__ == "__main__":

