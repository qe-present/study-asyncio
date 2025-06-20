import asyncio
import functools
import time
from typing import Callable,Any
async def delay(time:int)->int:
    print("睡"+str(time)+"秒")
    await asyncio.sleep(time)
    print("结束睡眠"+str(time)+"秒")
    return time

def async_timed():
    """
    装饰器，用于测量异步函数的执行时间。
    参数:
        func: 要装饰的异步函数。
    返回:
        包装后的异步函数，执行时会打印开始和结束时间以及耗时。
    """
    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'strarting {func} with args: {args}, kwargs: {kwargs}')
            start_time = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f'finished {func} in {elapsed_time:.2f} seconds')
        return wrapped
    return wrapper