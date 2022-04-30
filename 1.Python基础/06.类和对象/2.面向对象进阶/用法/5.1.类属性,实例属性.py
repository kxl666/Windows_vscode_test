# 类是一个特殊的对象,在内存中只有一份,使用一个类可以创建出很多个对象实例
# 存在类属性和类方法

# 对象创建后,内存中就有了一个对象的实实在在的存在,独立的内存空间 -- 实例
# 创建对象的动作叫做实例化

# 类属性就是针对类对象定义的属性


class People(object):
    country = 'china'  # 类属性


print(People.country)
p = People()
print(p.country)
p.country = 'japan'
print(p.country)  # 实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country  # 删除实例属性
print(p.country)

# 结果:
# china
# china
# japan
# china
# china
'''
如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用，会产生
一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，并且之后如果通过实例对象去
引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。
'''
