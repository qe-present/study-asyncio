from asyncio import Future,run
async def main():
    my_future = Future()
    print(f"future done: {my_future.done()}")
    my_future.set_result("hello")
    print(f"future done: {my_future.done()}")
    print(f"future result: {my_future.result()}")
if __name__ == '__main__':
    run(main())