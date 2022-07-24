import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

# 1. 删除一条数据
my_query = {"name": "Taobao"}
my_col.delete_one(my_query)

# 2. 删除多条数据
my_query = {"alexa": {"$gt": "100"}}
my_col.delete_many(my_query)
