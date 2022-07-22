# 以下俩个多态例子也关于对父类方法的重写
# 多态基于继承, 不同的子类对象调用相同的父类方法,产生不同的执行结果


class F1(object):

    def show(self):
        print('F1.show')


class S1(F1):

    def show(self):
        print('S1.show')


class S2(F1):

    def show(self):
        print('S2.show')


def Func(obj):  # 内部调用  传入不同的对象实参,就会产生不同的执行效果
    print(obj.show())


# s1_obj = S1()
# Func(s1_obj)

s2_obj = S2()
Func(s2_obj)
# s2_obj.show()  # 同4.2.多态.py,不需要再另外定义Func()
