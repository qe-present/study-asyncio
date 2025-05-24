import asyncio
async def hello_world()->str:
    await asyncio.sleep(1)
    return 'hello world'

async def main()->None:
    message=await hello_world()
    print(message)
if __name__ == '__main__':
    asyncio.run(main())
