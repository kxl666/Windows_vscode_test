import os

for folderName, subfolders, filenames in os.walk(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶'):
    print(f'The current folder is {folderName}')
    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folderName}: {subfolder}')
    for filename in filenames:
        print(f'FILE INSIDE {folderName}: {filename}')
    print('')

# 将输出目录,子目录,以及底层的文件名
