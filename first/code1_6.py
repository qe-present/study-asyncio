import time
import threading
def print_fib(number: int) -> None:
    def fib(n:int)-> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fib(n-1) + fib(n-2)
    print(f'fib({number}) = {fib(number)}')

def fibs_with_threading():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))
    fortieth_thread.start()
    forty_first_thread.start()
    fortieth_thread.join()
    forty_first_thread.join()
start=time.time()
fibs_with_threading()
end=time.time()
print(f'Time taken: {end-start:.4f} seconds')
"""
fib(40) = 63245986
fib(41) = 102334155
Time taken: 24.8322 seconds
由于GIL的存在，多线程并不能提高性能
"""
