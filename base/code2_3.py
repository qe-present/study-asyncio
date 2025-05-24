import asyncio
async def coroutine_add_one(number:int)->int:
    return number+1

if __name__ == '__main__':
    res=asyncio.run(coroutine_add_one(10))
    print(res)
"""
11
"""