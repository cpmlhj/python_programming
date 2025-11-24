import asyncio
import time
import random

async def worker(name, queue: asyncio.Queue):
    while True:
        sleep_for = await queue.get()

        # 休眠 sleep_for 秒
        await asyncio.sleep(sleep_for)

        # 通知队列 工作项已被执行

        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    
    # 创建一个用于存储工作项的队列
    queue = asyncio.Queue()

    total_sleep_time = 0

    # 生成随机段并将它们加入队列
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time  += sleep_for
        queue.put_nowait(sleep_for)

    # 创建三个工作项来并发处理 这个队列中20个任务
    tasks = []
    for t in range(3):
        task = asyncio.create_task(worker(f"worker-{t}", queue))
        tasks.append(task)

    # 等待队列
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at


    for t in tasks:
        t.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)   

    print("=====")
    print(f"3 workers slept in paralled for {total_slept_for:.2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds") 



if __name__ == '__main__':
    asyncio.run(main())


    