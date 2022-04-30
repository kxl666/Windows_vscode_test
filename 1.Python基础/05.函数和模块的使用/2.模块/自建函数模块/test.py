import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if m1.is_palindrome(num) and m2.is_prime(num):
        print('%d是回文素数' % num)
