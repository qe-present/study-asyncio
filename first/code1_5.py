import time

def print_fib(number: int) -> None:
    def fib(n:int)-> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fib(n-1) + fib(n-2)
    print(f'fib({number}) = {fib(number)}')

def fibs_no_threading():
    print_fib(40)
    print_fib(41)
start=time.time()
fibs_no_threading()
end=time.time()
print(f'Time taken: {end-start:.4f} seconds')
"""
fib(40) = 63245986
fib(41) = 102334155
Time taken: 24.8051 seconds
"""