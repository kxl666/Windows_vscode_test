# 1.配置文件参数
'''
port: 端口号,默认6379
bind: 允许的IP,默认只允许本机访问
time:  client空闲多少秒后关闭连接,默认0代表无限制
loglevel: 日志级别，分为: debug | verbose | notice |warning,默认为notice
logfile: 日志文件地址
syslog-enabled: 把日志记录到系统日志,默认yes
maxclients: 最大连接数，默认无限制
maxmemory: 占用内存的大小，默认无限制
appendonly: 开启AOF备份
appendfsync: AOF同步的频率，分为no | everysec | always
'''
# RDB与AOF存储方式的区别:
# RDB备份数据,AOF备份二进制binlog日志

# 2.连接
# 2.1.普通连接
import redis

# con = redis.Redis(host='45.43.61.98',
#                 port=6379,
#                 password='Hbxs@tpp@123!@#',
#                 db=0)

# 2.2.连接池连接
pool = redis.ConnectionPool(host='45.43.61.98',
                            port=6379,
                            password='Hbxs@tpp@123!@#',
                            db=0,
                            max_connections=10)
con = redis.Redis(connection_pool=pool)

con.set('name', '张三')
# 3.键(KEY)操作
# 3.1 删除
# con.delete('name')
# 3.2 检查是否存在
print(con.exists('name'))
# 3.3 获取键的类型
print(con.type('name'))
# 3.4 模糊匹配
# KEYS * 匹配 数据库 中所有 key 。
# KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
# KEYS hllo 匹配 hllo 和 heeeeello 等。
# KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo
print(con.keys('*'))
# 3.5 查看键的数量
print(con.dbsize())
# 3.6 查看键的列表
print(con.keys('*'))
# 3.7 设置键的过期时间
con.expire('name', 10)
# 3.8 获取键的过期时间
print(con.ttl('name'))
# 3.9 取消键的过期时间
con.persist('name')
# 3.10 重命名
con.rename('name', 'name2')
# 3.11 随机获取一个键
print(con.randomkey())
# 3.12 查看所有元素
con.sscan('name', '0')  # 分布式集合
# con.hscan('name', '0')  # 哈希类型
# con.zscan('name', '0')  # 列表类型
