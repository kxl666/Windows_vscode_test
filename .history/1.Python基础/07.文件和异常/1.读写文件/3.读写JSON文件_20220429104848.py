import json

# from msilib.schema import Directory


def main():
    myDirectory = {
        'name':
        '骆昊',
        'age':
        38,
        'qq':
        957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [{
            'brand': 'BYD',
            'max_speed': 180
        }, {
            'brand': 'Audi',
            'max_speed': 280
        }, {
            'brand': 'Benz',
            'max_speed': 320
        }]
    }
    try:
        with open(
                r"C:\Users\kxl666\Desktop\Python\1.Python基础\07.文件和异常\_temp\data.json",
                'w',
                encoding='utf-8') as fs:
            json.dump(myDirectory, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
