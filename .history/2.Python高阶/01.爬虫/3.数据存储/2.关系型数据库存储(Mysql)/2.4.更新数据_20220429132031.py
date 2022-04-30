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
