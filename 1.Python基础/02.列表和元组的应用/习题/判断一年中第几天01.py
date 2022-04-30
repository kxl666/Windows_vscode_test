# p2_1.py


def Day(year, month, day):
    month_data = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while month > 0:
        day += month_data[month - 1]
        month -= 1
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        day += 1
    return day


year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))

print("%d-%d-%d是第%d天" % (year, month, day, Day(year, month, day)))
