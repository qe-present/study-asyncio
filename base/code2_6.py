import asyncio
async def delay(time:int)->int:
    print("睡"+str(time)+"秒")
    await asyncio.sleep(time)
    print("结束睡眠"+str(time)+"秒")
