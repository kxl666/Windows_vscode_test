import pymysql

# 1.普通更新
db = pymysql.connect(host='45.43.61.98',
                     user='root',
                     password='Hbxs@tpp@123!@#',
                     db='spiders',
                     port=3006,
                     charset='utf8')

cursor = db.cursor()
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

db.close()

# 2.动态更新
# 以这里可以再实现一种去重的方法，如果数据存在， 则更新数据；如果数据不存在，则插入数据 另外，这种做法支持灵活的字典传值
