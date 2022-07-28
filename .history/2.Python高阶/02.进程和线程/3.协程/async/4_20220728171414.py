import asyncio
import time


async def say_after(delay, what):  # 协程函数
    await asyncio.sleep(delay)  # 延迟执行
    print(what)


async def main():
    # 01
    # task1 = asyncio.create_task(say_after(1, 'hello'))
    # task2 = asyncio.create_task(say_after(2, 'world'))
    # print(f"started at {time.strftime('%X')}")

    # await asyncio.gather(task1, task2)

    # print(f"finished at {time.strftime('%X')}")

    # 02
    task_list = [
        asyncio.create_task(say_after(1, 'hello')),
        asyncio.create_task(say_after(2, 'world'))
    ]


asyncio.run(main())
