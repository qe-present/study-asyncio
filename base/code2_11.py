import asyncio
from asyncio import CancelledError
from util import delay
async def main():
    long_task=asyncio.create_task(delay(10))
    seconds_elapsed=0
    while not long_task.done():
        print("任务还在运行")
        await asyncio.sleep(1)
        seconds_elapsed+=1
        if seconds_elapsed==5:
            print("取消任务")
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print("任务被取消")
if __name__ == '__main__':
    asyncio.run(main())
