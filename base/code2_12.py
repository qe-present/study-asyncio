import asyncio
from asyncio import CancelledError
from util import delay
async def main():
    long_task=asyncio.create_task(delay(10))
    try:
        result=await asyncio.wait_for(long_task,timeout=4)
        print(result)
    except asyncio.TimeoutError:
        print("任务超时")

if __name__ == '__main__':
    asyncio.run(main())
