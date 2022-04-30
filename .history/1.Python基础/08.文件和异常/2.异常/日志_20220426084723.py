# 日志模块还有级别设置DEBUG，INFO，WARNING，ERROR，CRITICAL，默认为WARNING
import logging

logging.basicConfig(filename=r'', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))

# logging.disable(logging.CRITICAL) # 禁用日志,使用后下面的日志不会输出
logging.info('End of program')
