from asyncio import Future
import asyncio


async def set_future_value(future):
    await asyncio.sleep(1)
    future.set_result("hello")


def make_request()->Future:
    future=Future()
    asyncio.create_task(set_future_value(future))
    return future

async def main():
    future=make_request()
    print(f"future done: {future.done()}")
    result=await future
    print(f"future done: {future.done()}")
    print(f"future result: {result}")

if __name__ == '__main__':
    asyncio.run(main())