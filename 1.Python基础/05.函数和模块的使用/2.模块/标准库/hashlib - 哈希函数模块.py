import hashlib

# 计算字符串"123456"的MD5摘要
print(hashlib.md5('123456'.encode()).hexdigest())

# 计算文件"的MD5摘要
hasher = hashlib.md5()  # 调用一个md5对象
with open(r"D:\Download\win7pack1ruanjian.zip", 'rb') as file:
    data = file.read(512)
    while data:
        hasher.update(data)  # update()方法，对参数进行加密，加密必须为bytes类型
        data = file.read(512)
print(hasher.hexdigest())  # 打印加密结果


# 一个简单的验证存储明文口令程序
def md5(arg):  # 这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5(bytes("abd", encoding="utf-8"))
    md5_pwd.update(bytes(arg, encoding="utf-8"))
    return md5_pwd.hexdigest()  # 返回加密的数据


def log(user, pwd):  # 登录时候的函数，由于md5不能反解， 因此登录的时候用正解
    with open(r"C:\Users\Administrator\Desktop\Python_all_file\user.txt",
              mode="r",
              encoding="utf-8") as f:
        for line in f:
            name, password = line.strip().split("|")  #
            # 登录的时候验证用户名以及加密的密码跟之前保存的是否一样
            if user == name and password == md5(pwd):
                return True


def register(user, pwd):  # 注册的时候把用户名和加密的密码写进文件，保存起来
    with open(r"C:\Users\Administrator\Desktop\Python_all_file\user.txt",
              mode="a",
              encoding="utf-8") as f:
        msg = user + "|" + md5(pwd) + "\n"
        f.write(msg)


if __name__ == '__main__':
    i = input("1表示登录，2表示注册").strip()
    if i == "2":
        user = input("用户名：")
        pwd = input("密码：")
        register(user, pwd)
    elif i == "1":
        user = input("用户名")
        pwd = input("密码：")
        r = log(user, pwd)  # 验证用户名和密码
        if r == "True":
            print("登录成功")
        else:
            print("登录失败")
    else:
        print("输入不合法")
