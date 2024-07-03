# 简单的Python应用程序中的进程和线程
import os
import threading
print(f'Process ID: {os.getpid()}')
total_threads = threading.active_count()
thread_name= threading.current_thread().name
print(f'Total threads: {total_threads}')
print(f'Current thread name: {thread_name}')