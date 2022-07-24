import pymongo

myclient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
mydb = myclient["runoobdb"]
dblist = myclient.list_database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")
