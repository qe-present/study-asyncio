import asyncio
async def coroutine_add_one(number:int)->int:
    return number+1

async def main():
    one=await coroutine_add_one(1)
    two=await coroutine_add_one(2)
    print(one)
    print(two)
if __name__ == '__main__':
    asyncio.run(main())
"""
2
3
"""