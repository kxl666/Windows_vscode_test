# 当实参是function(1,2,3)元组的形式那么 形参 args与*args 传入的 function(1,2,3) 没有区别
def fun(a, b, *args, **kwargs):
    print("a=", a)
    print("b=", b)
    print("args=", args)
    print("kwargs")
    for key, value in kwargs.items():
        print(key, "=", value)


fun(1, 2, 3, 4, 5, m=6, n=7, p=8)
print("--------------------------------")
fun(1, 2, 3, 4, 5, 6, 7, 8)
print("--------------------------------")
c = (3, 4, 5)
d = {"m": 6, "n": 7, "p": 8}
fun(1, 2, *c, **d)  # 解包操作
