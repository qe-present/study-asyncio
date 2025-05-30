import functools
import time
from typing import Callable,Any
def async_timed():
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