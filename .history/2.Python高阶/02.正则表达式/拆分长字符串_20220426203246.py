# split(pattern, string, maxsplit=0, flags=0) 用[正则表达式]指定的模式分隔符拆分字符串 返回列表
# 对于一个找不到匹配的字符串而言，split 不会对其作出分割，而是将其作为一个整体返回。

import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(len(sentence_list)
    while ('' in sentence_list):  #
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    main()
