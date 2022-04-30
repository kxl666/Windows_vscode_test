import pymysql

db = pymysql.connect(host='45.43.61.98',
                     user='root',
                     password='Hbxs@tpp@123!@#',
                     db='spiders',
                     port=3006,
                     charset='utf8')

cursor = db.cursor()
sql = 'SELECT * FROM EMPLOYEE WHERE AGE > %s' % (20)

# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行,返回一个元组

# 1.第一种
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     print(results)
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %
#               (fname, lname, age, sex, income))
# except Exception as e:
#     print(e)

# db.close()

# 2.第二种使用fetchone
# 避免数据量过大不使用fetchall
try:
    cursor.execute(sql)

except Exception as e:
    print(e)
