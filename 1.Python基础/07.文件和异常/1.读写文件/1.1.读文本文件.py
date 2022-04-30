import time


# 01 read()是读取所有字符
def main():
    f = None
    try:
        f = open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
                 'r',
                 encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()


# 02 通过with自动关闭文件
def main():
    try:
        with open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
                  'r',
                  encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()

# 03


def main():
    # 01 一次性读取整个文件内容
    with open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
              'r',
              encoding='utf-8') as f:
        print(f.read())

    # 02 通过for-in循环逐行读取
    with open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
              mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 03 读取文件按行读取到列表中readlines 是列表
    # 读取大文件时
    with open(
            r"C:\Users\Administrator\Desktop\Python_all_file\input.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(lines)

    # 04 一次只读一行readline(),例如有三行数据,则调用3次readline()才行
    with open(r"C:\Users\Administrator\Desktop\Python_all_file\input.txt",
              'r',
              encoding='utf-8') as f:
        print(f.readline())


if __name__ == '__main__':
    main()
