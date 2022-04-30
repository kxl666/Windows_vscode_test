import os

for folderName, subfolders, filenames in os.walk(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶'):
    # print('The current folder is ' + folderName)
    for subfolder in subfolders:
        # print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        with open(os.path.join(folderName, subfolder), 'w') as f:
            f.write('This is ' + subfolder)
            print(folderName + ': ' + subfolder + ' is created')
    # for filename in filenames:
    # print('FILE INSIDE ' + folderName + ': ' + filename)
    # print('')

# 将输出目录,子目录,以及底层的文件名
