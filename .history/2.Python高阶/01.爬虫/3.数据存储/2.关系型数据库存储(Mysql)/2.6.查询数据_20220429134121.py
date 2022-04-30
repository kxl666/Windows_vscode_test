import pymysql

db = pymysql.connect(host='45.43.61.98',
                     user='root',
                     password='Hbxs@tpp@123!@#',
                     db='spiders',
                     port=3006,
                     charset='utf8')

cursor = db.cursor()
sql = 'SELECT * FROM EMPLOYEE WHERE AGE > %s' % (20)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
except Exception as e:
    print(e)

db.close