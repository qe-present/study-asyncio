# 创建多个进程
import multiprocessing
import os

def hello_from_process():
    print(f'Hello from process {os.getpid()}')



if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()
    print(f'Hello from main process {os.getpid()}')
    hello_process.join()

"""
Hello from main process 8956
Hello from process 26852
"""