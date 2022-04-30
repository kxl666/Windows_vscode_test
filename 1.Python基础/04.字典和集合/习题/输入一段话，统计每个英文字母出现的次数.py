sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1  #
for key, value in counter.items():  #
    print('%s字母出现了%d次.' % (key, value))
