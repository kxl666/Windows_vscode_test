class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_false = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否为空
        if cls.instance is None:
            # 2. 调用父类的方法, 为第一个分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象的引用
        return cls.instance

    def __init__(self):

        # 4. 判断是否执行过初始化动作
        if MusicPlayer.init_false:
            return  # ruturn之后, 不会执行下面的代码

        # 5. 如果没有执行过初始化动作, 则执行初始化动作
        print("初始化")

        # 6. 修改类属性的标记
        MusicPlayer.init_false = True


# 创建多个对象
# 如果没有 1,2,3 则两个对象的引用十六进制地址不一样
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
# 如果没有 4,5,6 则会输出两次 "初始化"
