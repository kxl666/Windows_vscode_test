import threading
import time

lock = threading.Lock()


class Account:

    def __init__(self, balance):
        self.banlance = balance


def draw(account, amount):
    with lock:  # 这是更方便的上锁方式,不需要自己手动上锁(acquire)和解锁(release)
        if account.banlance >= amount:
            # time.sleep(0.1)  # 在没上锁情况下,添加等待时间(阻塞)后,余额会一直-600
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
