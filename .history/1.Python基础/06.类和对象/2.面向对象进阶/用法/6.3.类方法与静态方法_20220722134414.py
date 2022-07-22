import re


class People:
def _init__(self, name,age) :
self.name = name
self.age = age
def introduce_myself(self):
print(f'大家好，我叫: {self.name} ' )
staticmethod
def add_two_string_num(a, b ):
a_int = int(a)
b_int = int(b)
return a_int + b_int
aclassmethod
def from_chinese_string(cls, sentence) :
name = re.search('名字:(.*?), ', content).group( 1)age = re.search('年龄:(\d+) ' , content).group(1)return cls(name, age)
classmethod
def from_english_string(cls, sentence):
name = re.search( 'name: (.*?), ', content).group(1)age = re.search( 'age: (\d+) ' , content).group(1)return cls (name, age)
def calc_age_after_n_year(self, n) :
age = People.add_two_string_num(self.age,n)print(f'{n}年以后，我{age}岁")
content = 'my name: kinganme,my age: 15 please extract them'kingname = People.from_english_string(content)
kingname.introduce_myself( )
kingname.calc_age_after_n_year( 10)
