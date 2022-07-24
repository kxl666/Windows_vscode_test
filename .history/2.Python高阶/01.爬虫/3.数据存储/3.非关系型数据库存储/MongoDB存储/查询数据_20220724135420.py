import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
mydb = myClient['mydatabase']
mycol = mydb["sites"]
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)
print(x.inserted_id)
