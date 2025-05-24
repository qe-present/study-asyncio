import asyncio
from util import delay
async def add_one(number:int)->int:
    return number + 1
async def hello_world()->str:
    await delay(3)
    return 'hello world'
async def main():
    message=await hello_world()
    one=await add_one(1)
    print(message)
    print(one)
if __name__ == '__main__':
    asyncio.run(main())
"""
睡1秒
结束睡眠1秒
hello world
2
"""