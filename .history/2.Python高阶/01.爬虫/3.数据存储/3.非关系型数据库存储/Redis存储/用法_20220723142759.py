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

r = redis.Redis(host='45.43.61.98',
                port=6379,
                password='Hbxs@tpp@123!@#',
                db=0)
print(r)
