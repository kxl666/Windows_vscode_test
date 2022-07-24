import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

# 1. 修改一条数据
my_query = {"alexa": "10000"}
new_values = {"$set": {"alexa": "12345"}}
