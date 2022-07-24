import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]
my_dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = my_col.insert_one(my_dict)
print(x.inserted_id)
my_col.delete_one(my_dict)
print(my_col.count_documents({}))
