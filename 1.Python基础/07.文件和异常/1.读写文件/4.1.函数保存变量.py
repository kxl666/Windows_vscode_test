# 假定你有一个字典，保存在一个变量中，你希望保存这个变量和它的内容，以便将来使用。
# pprint.pformat()函数将提供一个字符串，你可以将它写入.py 文件。该文件将成为你自己的模块，如果你需要使用存储在其中的变量，就可以导入它

import pprint

cats = [{
    'name': 'Zophie',
    'desc': 'chubby'
}, {
    'name': 'Pooka',
    'desc': 'fluffy'
}]
pprint.pprint(cats)
# 结果：
# [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
fileObj = open(
    r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\1.读写文件\myCats.py',
    'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
