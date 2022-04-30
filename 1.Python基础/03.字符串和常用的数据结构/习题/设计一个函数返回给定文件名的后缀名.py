from os.path import splitext

# def get_suffix(filename):
#     """获取文件名的后缀名
#     :param filename: 文件名
#     :return: 文件的后缀名
#     """
#     # 从字符串中逆向查找.出现的位置
#     pos = filename.rfind('.')
#     # 通过切片操作从文件名中取出后缀名
#     return filename[pos + 1:] if pos > 0 else ''  # 用法


def get_suffix(filename):
    return splitext(filename)[1][1:]  # os.path针对路径名的操作


print(get_suffix('readme.txt'))  # txt
print(get_suffix('readme.txt.md'))  # md
print(get_suffix('.readme'))  #
print(get_suffix('readme.'))  #
print(get_suffix('readme'))  #
