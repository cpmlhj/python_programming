import queue
import threading
import time
import random


def worker(name, work_queue: queue.Queue):
    """多线程版本的 worker"""
    while True:
        # 从队列获取任务（阻塞式，会等待直到有任务）
        sleep_for = work_queue.get()
        
        # 如果收到 None，表示结束信号
        if sleep_for is None:
            work_queue.task_done()
            break
        
        # 休眠 sleep_for 秒（这会阻塞线程）
        time.sleep(sleep_for)
        
        # 通知队列任务已完成
        work_queue.task_done()
        
        print(f'{name} has slept for {sleep_for:.2f} seconds')


def main():
    # 创建一个线程安全的队列
    work_queue = queue.Queue()
    
    total_sleep_time = 0
    
    # 生成随机睡眠时间并加入队列
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        work_queue.put(sleep_for)
    
    # 创建三个工作线程来并行处理队列中的20个任务
    threads = []
    for i in range(3):
        thread = threading.Thread(
            target=worker, 
            args=(f"worker-{i}", work_queue),
            daemon=True  # 守护线程，主程序退出时自动结束
        )
        thread.start()
        threads.append(thread)
    
    # 等待队列中所有任务完成
    started_at = time.monotonic()
    work_queue.join()  # 阻塞直到所有任务完成
    total_slept_for = time.monotonic() - started_at
    
    # 向所有线程发送结束信号
    for _ in threads:
        work_queue.put(None)  # 发送结束信号
    
    # 等待所有线程结束
    work_queue.join()  # 等待所有线程处理完结束信号
    for thread in threads:
        thread.join()  # 确保线程完全退出
    
    print("=====")
    print(f"3 workers slept in parallel for {total_slept_for:.2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds")


if __name__ == '__main__':
    main()
