import asyncio
from util import delay
def call_later():
    print("call later")
async def main():
    loop=asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

if __name__ == '__main__':
    asyncio.run(main(),debug=True)
