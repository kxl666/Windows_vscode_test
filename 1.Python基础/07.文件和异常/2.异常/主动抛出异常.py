def input_password():
    password = input('请输入密码：')
    if len(password) >= 6:
        return password
    # 如果输入的密码小于6位，则抛出异常
    print('主动抛出异常')
    # 1. 创建异常对象
    ex = Exception('密码长度不够')
    # 2. 主动抛出异常
    raise ex


# 定义函数，调用input_password()
try:
    print(input_password())
except Exception as result:
    print(result)
