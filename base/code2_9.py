import asyncio
from util import delay
async def main():
    sleep_for_three=asyncio.create_task(delay(3))
    sleep_for_again=asyncio.create_task(delay(3))
    sleep_for_once_more=asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_for_again
    await sleep_for_once_more

if __name__ == '__main__':
    asyncio.run(main())
