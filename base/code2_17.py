import asyncio
from util import async_timed
@async_timed()
async def delay(delay_seconds:int)->int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} seconds')
    return delay_seconds
@async_timed()
async def main():
    task1 = asyncio.create_task(delay(2))
    task2 = asyncio.create_task(delay(3))
    await task1
    await task2
if __name__ == '__main__':
    asyncio.run(main())
"""
finished sleeping for 2 seconds
finished <function delay at 0x000001FAD93FBB00> in 2.00 seconds
finished sleeping for 3 seconds
finished <function delay at 0x000001FAD93FBB00> in 3.01 seconds
finished <function main at 0x000001FAD9A4C860> in 3.01 seconds
"""