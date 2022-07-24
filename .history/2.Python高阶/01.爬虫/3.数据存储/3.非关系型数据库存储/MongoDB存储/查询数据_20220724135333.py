import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
mydb = myClient['mydatabase']
mycol = mydb["sites"]
dbList = myClient.list_database_names()
print(dbList)
