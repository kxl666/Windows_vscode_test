class base(object):

    def test(self):
        print('----base test----')


class A(base):

    def test(self):
        print('----A test----')


# 定义一个父类
class B(base):

    def test(self):
        print('----B test----')


# 定义一个子类，继承自A、B
class C(A, B):
    pass


obj_C = C()
obj_C.test()

# 如果在上面的多继承例子中，如果父类A和父类B中，有一个同名的方法，那么通过子类去调用的时候，调用的是父类A的方法，而不是父类B的方法,谁在前先调用谁。
print(C.__mro__)  # 可以查看C类的对象搜索方法时的先后顺序

# 如果父类之间存在同名的属性或者方法,应该避免使用多继承
