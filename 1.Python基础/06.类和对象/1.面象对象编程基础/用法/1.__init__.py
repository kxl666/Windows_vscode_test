class Cat:

    def __init__(self):
        print("这是一个初始化方法")
        self.name = "Tom"
        # 这种方法会将属性name写死， 如果想创建对象时就设置对象的属性
        # 应该 def __init__(self, name)


# 使用类创建对象的时候,会自动调用初始化方法__init__
tom = Cat()  # 会输出print的内容
