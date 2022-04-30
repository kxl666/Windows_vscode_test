# 定义一个home类


class Home:

    def __init__(self, area):
        self.area = area  # 房间剩余面积
        self.containsItem = []  # 房间中的物品

    def __str__(self):
        msg = "房间剩余面积：%s" % self.area
        if len(self.containsItem) > 0:
            msg += "\n房间中的物品："
            for temp in self.containsItem:
                msg += temp.getName() + ", "
            msg = msg.strip(", ")

        return msg

    def accommodate(self, item):  # 内部调用
        if self.area >= item.getArea():
            self.containsItem.append(item)
            self.area -= item.getArea()
            print("ok: 已经存放入房间中")
        else:
            print("error:房间可用面积为:%d,但当前存放物品需要面积为%d" %
                  (self.area, item.getArea()))


# 定义bed类


class Bed:

    def __init__(self, area, name='床'):
        self.area = area
        self.name = name

    def __str__(self):
        msg = "床的面积为:%s" % self.area
        return msg

    def getArea(self):
        return self.area

    def getName(self):
        return self.name


newHome = Home(100)
print(newHome)
newBed = Bed(10, '被子')
print(newBed)
newHome.accommodate(newBed)
print(newHome)
