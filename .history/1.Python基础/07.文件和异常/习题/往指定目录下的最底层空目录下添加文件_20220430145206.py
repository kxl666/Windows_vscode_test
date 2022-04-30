import os

for folderName, subfolders, filenames in os.walk(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶\06.GUI'):
    for subfolder in subfolders:
        # if len(os.listdir(folderName + '\\' + subfolder)) == 0: # 第一种判断文件夹是否为空
        if not any([True for _ in os.scandir(folderName + '\\' + subfolder)
                    ]):  # 第二种判断文件夹是否为空
            with open(os.path.join(folderName, subfolder) + '\\temp.txt',
                      'w') as f:
                f.write('This is ' + subfolder)
                print(folderName + ': ' + subfolder + '\\temp.txt' +
                      ' is created')
