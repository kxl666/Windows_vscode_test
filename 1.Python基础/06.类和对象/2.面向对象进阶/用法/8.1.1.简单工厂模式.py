# 1.1.使用函数实现


# 定义伊兰特车类
class YilanteCar01(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义索纳塔车类
class SuonataCar01(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 用来生成具体的对象
def createCar(typeName):
    if typeName == "伊兰特":
        car = YilanteCar01()
    elif typeName == "索纳塔":
        car = SuonataCar01()
    return car


# 定义一个销售北京现代车的店类
class CarStore01(object):

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        car = createCar(typeName)
        return car
