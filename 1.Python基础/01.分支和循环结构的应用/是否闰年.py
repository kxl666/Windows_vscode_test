# p2_1.py


def Year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, ":是闰年！")


year = int(input("请输入年份:"))
Year(year)
