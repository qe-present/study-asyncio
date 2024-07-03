# 创建多线程Python应用程序
import threading
def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}')
hello_thread=threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name= threading.current_thread().name
print(f'Total threads: {total_threads}')
print(f'Current thread name: {thread_name}')

hello_thread.join()
"""
Hello from thread <Thread(Thread-1 (hello_from_thread), started 13204)>Total threads: 2
Current thread name: MainThread

"""