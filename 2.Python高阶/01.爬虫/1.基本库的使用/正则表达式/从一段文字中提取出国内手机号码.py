# 01 search(pattern, string, flags=0)	搜索字符串中 第一次 出现正则表达式的模式 成功返回[匹配对象] 否则返回None ,需要使用匹配对象的一些方法才能获得需要的内容，例如group()
# re.match与re.search的区别：
#   re.match 只匹配字符串的开始，如果字符串[开始]不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配[整个]字符串，直到找到一个匹配。
# 02 findall(pattern, string, flags=0)	查找字符串 所有 与正则表达式匹配的模式 返回字符串的 列表
# 03 finditer(pattern, string, flags=0)	查找字符串 所有 与正则表达式匹配的模式 返回一个 迭代器
import re


def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')  # 注意括号,group以括号来区分
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    # findall也将括号内的内容保存到一个列表中
    mylist = pattern.findall(sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 01 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 02 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,
                           m.end())  # 用法 每次移动到下一个匹配对象位置,因为search只匹配一次


if __name__ == '__main__':
    main()
