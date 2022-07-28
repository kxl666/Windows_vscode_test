import asyncio
import time


async def say_after(delay, what):  # 协程函数
    await asyncio.sleep(delay)  # 延迟执行
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

# 耗时2秒,使用create_task直接将coroutine转化为task,并且把task注册到event loop里面。所以分担了await的一些功能
