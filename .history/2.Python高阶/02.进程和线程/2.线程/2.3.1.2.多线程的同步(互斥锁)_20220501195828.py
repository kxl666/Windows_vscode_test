import threading


class Account:

    def __init__(self, balance):
        self.banlance = balance


def draw(account, amount):
    if account.banlance >= amount:
        time.sleep(0.1)
        print(threading.current_thread().name, '取钱成功')
        account.banlance -= amount
        print(threading.current_thread().name, '取钱后余额为', account.banlance)
    else:
        print(threading.current_thread().name, '取钱失败')


if __name__ == '__main__':
    account = Account(1000)
    t1 = threading.Thread(target=draw, args=(account, 800))
    t2 = threading.Thread(target=draw, args=(account, 800))
    t1.start()
    t2.start()
