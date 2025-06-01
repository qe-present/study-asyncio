import asyncio
import requests
from util import async_timed
@async_timed()
async def get_example_status()->int:
    return requests.get('https://example.com').status_code

@async_timed()
async def main():
    task1 = asyncio.create_task(get_example_status())
    task2 = asyncio.create_task(get_example_status())
    task3= asyncio.create_task(get_example_status())
    await task1
    await task2
    await task3
if __name__ == '__main__':
    asyncio.run(main())
"""
strarting <function main at 0x000002840ECA9120> with args: (), kwargs: {}
strarting <function get_example_status at 0x000002840EB07560> with args: (), kwargs: {}
finished <function get_example_status at 0x000002840EB07560> in 1.13 seconds
strarting <function get_example_status at 0x000002840EB07560> with args: (), kwargs: {}
finished <function get_example_status at 0x000002840EB07560> in 1.03 seconds
strarting <function get_example_status at 0x000002840EB07560> with args: (), kwargs: {}
finished <function get_example_status at 0x000002840EB07560> in 1.07 seconds
finished <function main at 0x000002840ECA9120> in 3.23 seconds
"""