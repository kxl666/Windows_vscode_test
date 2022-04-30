# 1.2.使用类来实现


# 定义伊兰特车类
class YilanteCar02(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义索纳塔车类
class SuonataCar02(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义一个生产汽车的工厂，让其根据具体的订单生产车
class CarFactory(object):

    def createCar(self, typeName):
        if typeName == "伊兰特":
            car = YilanteCar02()
        elif typeName == "索纳塔":
            car = SuonataCar02()

        return car


# 定义一个销售北京现代车的店类
class CarStore02(object):

    def __init__(self):
        # 设置4s店的指定生产汽车的工厂
        self.carFactory = CarFactory()

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        car = self.carFactory.createCar(typeName)
        return car
