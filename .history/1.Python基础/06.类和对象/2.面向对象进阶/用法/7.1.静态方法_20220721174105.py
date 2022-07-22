# 既不需要访问实例属性或者调用实例方法
# 也不需要访问类属性或者调用类方法
# 此时可以用上 静态方法@staticmethod
# 也就是静态方法不可继承


class Dog(object):

    @staticmethod
    def run():  # 静态方法可以不需要参数
        print("小狗要跑...")


# 通过类名.调用静态方法,不需要实例化对象
Dog.run()
