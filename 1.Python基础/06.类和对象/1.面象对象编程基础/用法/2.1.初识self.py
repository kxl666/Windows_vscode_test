class Cat:

    # 哪一个对象调用的方法, self就是哪一个对象的引用
    def eat(self):  # 这里传参可以不用指定name，即def eat(self, name)
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.name = "tom"  # 不建议在类的外部给对象增加属性，应该封装在类的内部
tom.eat()
tom.drink()
