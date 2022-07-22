# 可以看到，通过在 CLanguage 类中实现 __call__() 方法，使的 clangs 实例对象变为了可调用对象。


class CLanguage:
    # 定义__call__方法
    def __call__(self, name, add):
        print("调用__call__()方法", name, add)


clangs = CLanguage()
# clangs("C语言中文网", "http://c.biancheng.net")
# 对比正常调用类方法的方式 结果是一样的
clangs.__call__("C语言中文网", "http://c.biancheng.net")
