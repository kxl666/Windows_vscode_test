import asyncio
import threading
import time

import httpx

client = httpx.AsyncClient()  # 创建一个httpx客户端


async def async_main(url, sign):
    response = await client.get(url)
    status_code = response.status_code
    print(f'async_main: {threading.current_thread()}: {sign}:{status_code}')


loop = asyncio.get_event_loop()
tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(200)]
async_start = time.time()
# 01
# loop.run_until_complete(asyncio.wait(tasks))
# 02
loop.run_until_complete(asyncio.gather(*tasks))
async_end = time.time()
# loop.close()
print(async_end - async_start)
