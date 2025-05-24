import asyncio
from util import delay
async def main():
    sleep_three=asyncio.create_task(delay(3))
    print(type(sleep_three))
    result = await sleep_three
    print(result)
if __name__ == '__main__':
    asyncio.run(main())
"""
<class '_asyncio.Task'>
睡3秒
结束睡眠3秒
3
"""