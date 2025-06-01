import asyncio
from util import async_timed
@async_timed()
async def cpu_bound_work()->int:
    counter= 0
    for i in range(10**8):
        counter += i
    return  counter
@async_timed()
async def main():
    task1 = asyncio.create_task(cpu_bound_work())
    task2 = asyncio.create_task(cpu_bound_work())
    await task1
    await task2
if __name__ == '__main__':
    asyncio.run(main())

"""
finished <function cpu_bound_work at 0x000001445859BB00> in 3.12 seconds
strarting <function cpu_bound_work at 0x000001445859BB00> with args: (), kwargs: {}
finished <function cpu_bound_work at 0x000001445859BB00> in 2.88 seconds
finished <function main at 0x0000014458C1C860> in 6.00 seconds
"""