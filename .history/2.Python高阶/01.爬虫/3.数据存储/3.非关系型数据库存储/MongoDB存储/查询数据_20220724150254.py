import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

# 1.查询一条数据
print(my_col.find_one(), '_____________')

# 2.查询多条数据
for x in my_col.find():
    print(x)

# 3. 指定id查询数据
print(my_col.find_one({"_id": 3}), '_____________')

# 4. 查询指定字段
print(my_col.find_one({"name": "Zhihu"}), '_____________')

# 5. 查询指定字段值
for x in my_col.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)
# 将要返回的字段对应值设置为 1，其他字段设置为 0

# 6. 根据指定条件查询数据
my_query = {"name": "Taobao"}
for x in my_col.find(my_query):
    print(x, '_____________')

# 7. 高级查询...
my_query = {"name": {"$gt": "H"}}  # 查询 name 字段大于 H 的数据
for x in my_col.find(my_query):
    print(x, '_____________')

# 8. 使用正则表达式查询
my_query = {"name": {"$regex": "^T"}}  # 查询 name 字段以 T 开头的数据
for x in my_col.find(my_query):
    print(x, '_____________')

# 9.
