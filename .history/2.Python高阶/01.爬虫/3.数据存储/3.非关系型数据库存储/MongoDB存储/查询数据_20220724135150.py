import pymongo

myclient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
mydb = myclient['mydatabase']
dblist = myclient.list_database_names()
print(dblist)