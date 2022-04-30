# 烤地瓜的类


class SweetPotato:

    # 定义初始化方法

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    # 定制显示内容

    def __str__(self):
        msg = self.cookedString + "地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("
            for temp in self.condiments:
                msg = msg + temp + ","

            msg = msg.strip(",")
            msg = msg + ")"
        return msg

    # 定制烤地瓜方法

    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤的"
        elif self.cookedLevel > 5:
            self.cookedString = "半烤的"
        elif self.cookedLevel > 3:
            self.cookedString = "煎的"
        elif self.cookedLevel > 0:
            self.cookedString = "生的"
        else:
            self.cookedString = "熟的"

    # 定制地瓜添加调料方法

    def addCondiments(self, condiments):
        self.condiments.append(condiments)


Potato1 = SweetPotato()
print(Potato1)  # 生的地瓜
# 开始烤地瓜
Potato1.cook(4)
print(Potato1)  # 煎的地瓜
# 开始添加调料
Potato1.addCondiments("盐")
print(Potato1)  # 煎的地瓜(盐)
