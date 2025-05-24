async def coroutine_add_one(number:int)->int:
    return number+1
def add_one(number:int)->int:
    return number+1
res=add_one(1)
coro_res=coroutine_add_one(res)
print(res)
print(coro_res)
"""
2
<coroutine object coroutine_add_one at 0x0000015A26265B40>
<sys>:0: RuntimeWarning: coroutine 'coroutine_add_one' was never awaited
"""