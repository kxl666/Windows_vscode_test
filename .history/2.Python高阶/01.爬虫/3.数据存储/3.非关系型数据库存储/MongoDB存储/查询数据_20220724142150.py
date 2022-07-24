import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

# 1.查询一条数据
print(my_col.find_one())

# 2.查询多条数据
for x in my_col.find():
    print(x)
