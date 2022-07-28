# async 没有提升运算速度，比较适合处理需要等待的事情，比如网络请求。适合处理I/O密集型的任务。
# 在await后面只能跟三种可等待的对象：协程对象、future对象、task对象。
# 使用 await 可以将耗时等待的操作挂起，让出控制权。当协程执行的时候遇到 await，时间循环就会将本协程挂起，转而去执行别的协程，直到其他的协程挂起或执行完毕。
import asyncio
import time


async def say_after(delay, what):  # 协程函数
    await asyncio.sleep(delay)  # 延迟执行
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

# 耗时3秒,因为await需要将corou