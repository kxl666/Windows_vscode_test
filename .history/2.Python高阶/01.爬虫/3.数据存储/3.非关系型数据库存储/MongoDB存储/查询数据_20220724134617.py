import pymongo

myclient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
mydb = myclient["runoobdb"]