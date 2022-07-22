class Tool(object):
    # 使用赋值语句定义类属性,记录所有工具对象的数量
    Count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.Count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("钉子")

print(Tool.Count)
# 输出3

# print(tool3.Count)
# 不建议对象.类属性,参考7.1.类属性,实例属性.py
