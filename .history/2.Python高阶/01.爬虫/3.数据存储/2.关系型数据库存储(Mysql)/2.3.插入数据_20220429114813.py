import pymysql

# 第一种插入数据的方法
# db = pymysql.connect(host='45.43.61.98',
#                      user='root',
#                      password='Hbxs@tpp@123!@#',
#                      db='spiders',
#                      port=3006,
#                      charset='utf8')

# cursor = db.cursor()
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except Warning as e:
#     # 如果发生错误则回滚
#     print(e)
#     db.rollback()

# # 关闭数据库连接
# db.close()

# 第二种插入数据的方法
db = pymysql.connect(host='45.43.61.98',
                     user='root',
                     password='Hbxs@tpp@123!@#',
                     db='spiders',
                     port=3006,
                     charset='utf8')
