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

my_query = {"name": {"$regex": "^F"}}
my_col.delete_many(my_query)

# 3. 删除集合中的所有文档
my_col.delete_many({})

# 4. 删除集合
# 4.1 第一种方式
my_db.drop_collection("sites")
# 4.2 第二种方式
my_col.drop()
