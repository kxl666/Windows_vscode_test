import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

# 1. 修改一条数据
my_query = {"alexa": "100"}
new_values = {"$set": {"alexa": "12345"}}
my_col.update_one(my_query, new_values)

# 2. 修改多条数据
my_query = {"alexa": {"$gt": "100"}}
new_values = {"$set": {"alexa": "12345"}}
my_col.update_many(my_query, new_values)
