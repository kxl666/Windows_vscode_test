# 定义一个父类，如下:
class Cat(object):

    def __init__(self, name, color="白色"):
        self.name = name
        self.color = color

    def run(self):
        print(f"{self.name}--在跑")


# 定义一个子类，继承Cat类如下:
class Bosi(Cat):

    def setNewName(self, newName):
        self.name = newName

    def eat(self):
        print(f"{self.name}--在吃")


bs = Bosi("印度猫")
print(f'bs的名字为:{bs.name}')
print(f'bs的颜色为:{bs.color}')
bs.eat()
bs.setNewName('波斯')
bs.run()

# 结果:
'''
bs的名字为:印度猫
bs的颜色为:白色
印度猫--在吃
波斯--在跑
'''
# 虽然子类没有定义__init__方法，但是父类有，所以在子类继承父类的时候这个方法就被继承了，所以只要创建Bosi的对象，就默认执行了那个继承过来的__init__方法
