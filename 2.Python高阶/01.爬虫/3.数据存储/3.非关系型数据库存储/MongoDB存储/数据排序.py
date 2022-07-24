import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

for x in my_col.find().sort("alexa", -1):  # 按照 alexa 字段降序排序
    print(x)
