import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


asyncio.run(main())  # 需要此方式才能执行协程函数
