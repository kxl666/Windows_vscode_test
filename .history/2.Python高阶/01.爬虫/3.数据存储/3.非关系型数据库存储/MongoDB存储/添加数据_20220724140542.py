import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]
my_dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = my_col.insert_one(my_dict)  # 插入一条数据
print(x.inserted_id)  # 返回
for x in my_col.find():  # 查询所有数据
    print(x)
