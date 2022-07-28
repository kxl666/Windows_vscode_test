# async 没有提升运算速度，比较适合处理需要等待的事情，比如网络请求。适合处理I/O密集型的任务。

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
