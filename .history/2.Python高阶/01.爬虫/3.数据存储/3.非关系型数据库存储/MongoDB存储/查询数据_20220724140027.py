import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]
my_dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = my_col.insert_one(my_dict)
for x in my_col.find():
    print(x)
# my_col.drop()
# for x in my_col.find():
#     print(x)
