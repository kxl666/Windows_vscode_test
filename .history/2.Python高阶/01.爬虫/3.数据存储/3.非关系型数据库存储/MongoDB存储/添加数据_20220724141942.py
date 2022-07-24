import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]
my_dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

# 1. 插入一条数据
x = my_col.insert_one(my_dict)  # 插入一条数据
print(x.inserted_id)  # 返回 inserted_id 属性，它是插入文档的 id 值
for x in my_col.find():  # 查询所有数据
    print(x)
my_col.delete_many({})  # 删除所有数据

# 2. 插入多条数据
my_dicts = [{
    "name": "Taobao",
    "alexa": "100",
    "url": "https://www.taobao.com"
}, {
    "name": "QQ",
    "alexa": "101",
    "url": "https://www.qq.com"
}, {
    "name": "Facebook",
    "alexa": "10",
    "url": "https://www.facebook.com"
}, {
    "name": "知乎",
    "alexa": "102",
    "url": "https://www.zhihu.com"
}]

my_col.insert_many(my_dicts)  # 插入多条数据
for x in my_col.find():
    print(x)

my_col.delete_many({})

# 3.指定id插入数据
my_dicts = [{
    "_id": 1,
    "name": "RUNOOB",
    "cn_name": "菜鸟教程"
}, {
    "_id": 2,
    "name": "Google",
    "address": "Google 搜索"
}, {
    "_id": 3,
    "name": "Facebook",
    "address": "脸书"
}, {
    "_id": 4,
    "name": "Taobao",
    "address": "淘宝"
}, {
    "_id": 5,
    "name": "Zhihu",
    "address": "知乎"
}]

my_col.insert_many(my_dicts)
for x in my_col.find():
    print(x)