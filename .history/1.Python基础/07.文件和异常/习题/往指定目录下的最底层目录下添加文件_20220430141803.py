import os

for folderName, subfolders in os.walk(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶'):
    for subfolder in subfolders:
        print(subfolder)

        # with open(os.path.join(folderName, subfolder) + '\\temp.txt',
        #           'w') as f:
        #     f.write('This is ' + subfolder)
        #     print(folderName + ': ' + subfolder + '\\temp.txt' + ' is created')
