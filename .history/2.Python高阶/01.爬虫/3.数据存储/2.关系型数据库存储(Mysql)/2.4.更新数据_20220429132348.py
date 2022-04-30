import pymysql

db = pymysql.connect(host='45.43.61.98',
                     user='root',
                     password='Hbxs@tpp@123!@#',
                     db='spiders',
                     port=3006,
                     charset='utf8')
# 1.普通更新
# cursor = db.cursor()
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()

# db.close()

# 2.动态更新
# 以这里可以再实现一种去重的方法，如果数据存在， 则更新数据；如果数据不存在，则插入数据 另外，这种做法支持灵活的字典传值
cursor = db.cursor()

data = {
    'FIRST_NAME': 'kxl',
    'LAST_NAME': 'kxl666',
    'AGE': 20,
    'SEX': 'F',
    'INCOME': 2000
}
table = 'EMPLOYEE'
keys = ", ".join(data.keys())
values = ", ".join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,
                                                             keys=keys,
                                                             values=values)
try:
    # 执行sql语句
    cursor.execute(sql, tuple(data.values()))
    # 提交到数据库执行
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    print(e)
    db.rollback()

# 关闭数据库连接
db.close()