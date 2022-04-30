import random
import string

ALL_CHARS = string.digits + string.ascii_letters  # 用法


def generate_code(code_len=4):
    """生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.sample(ALL_CHARS, k=code_len))  #
    """
    说明：random模块的sample和choices函数都可以实现随机抽样，
    sample实现无放回抽样，这意味着抽样取出的字符是不重复的；
    choices实现有放回抽样，这意味着可能会重复选中某些字符。
    这两个函数的第一个参数代表抽样的总体，而参数k代表抽样的数量
    """


for _ in range(10):
    print(generate_code())
    print(ALL_CHARS)

for _ in range(10):
    print(generate_code())
