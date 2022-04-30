"""
计算指定的年月日是这一年的第几天

Version: 0.1
Author: 骆昊
"""


def is_leap_year(year):
    """判断指定的年份是不是闰年，平年返回False，闰年返回True"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    """
    # 用嵌套的列表保存平年和闰年每个月的天数
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    # 布尔值False和True可以转换成整数0和1，因此
    # 平年会选中嵌套列表中的第一个列表(2月是28天)
    # 闰年会选中嵌套列表中的第二个列表(2月是29天)
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date


print(which_day(1980, 11, 28))  # 333
print(which_day(1981, 12, 31))  # 365
print(which_day(2018, 1, 1))  # 1
print(which_day(2016, 3, 1))  # 61
