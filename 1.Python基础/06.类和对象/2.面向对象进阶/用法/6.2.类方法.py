class People(object):
    country = 'china'

    # 类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):  # 类方法还有一个用途就是可以对类属性进行修改
        cls.country = country


p = People()
print(People.getCountry())  # 可以通过类对象引用

p.setCountry('japan')

print(p.getCountry())
print(People.getCountry())
