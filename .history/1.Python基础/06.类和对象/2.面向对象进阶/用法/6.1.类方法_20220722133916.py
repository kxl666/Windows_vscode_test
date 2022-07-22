# 类方法就是针对类对象定义的方法
# 类方法需要用修饰器(装饰器)classmethod来标识,告诉解释器这是一个类方法
# 类方法的第一个参数应该是cls
#  由哪一个类调用的方法,方法内的cls就是哪一个类的引用。这个参数和实例方法的第一个参数是self类似
#  使用其他名称也可以。不过习惯使用cls
#  通过类名,调用类方法,调用方法时。不需要传递cls参致
#  在方法内部可以通过cls,访问类的属性  也可以通过cls.调用其他的类方法


# 当你想使用工厂模式，根据不同的参数生成同一个类的不同对象的时候，就可以使用类方法
class Tool(object):
    # 使用赋值语句定义类属性,记录所有工具对象的数量
    Count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量: %d" % cls.Count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.Count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("钉子")

# 调用类方法
Tool.show_tool_count()  # 可以通过类对象引用
tool3.show_tool_count()  # 也可以用过实例对象引用
