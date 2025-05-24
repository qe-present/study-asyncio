[TOC]



```markmap
---
markmap:
  zoom: false
  pan: false
  height: 300px
  backgroundColor: "#f8f8f8"
---

# 关于协程
## 创建协程
## 比较普通函数
## 执行协程
## await 关键字暂停执行
## 使用sleep
## 运行两个协程
# 通过任务并行
## ch
```

# 关于协程

可将协程想象成一个普通的Python函数，但它具有在遇到可能需要一段时间才能
完成的操作时，暂停执行的超能力
## 创建协程
使用`async`将函数标记为协程
```python
async def my_coroutine()->None:
    print("hello world")
```
##  比较普通函数
```python
async def coroutine_add_one(number:int)->int:
    return number+1
def add_one(number:int)->int:
    return number+1
res=add_one(1)
coro_res=coroutine_add_one(res)
print(res)
print(coro_res)
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
```
可以发现协程没有执行，返回一个协程对象
## 执行协程
```python
import asyncio
async def coroutine_add_one(number:int)->int:
    return number+1

if __name__ == '__main__':
    res=asyncio.run(coroutine_add_one(10))
    print(res)
import asyncio
async def coroutine_add_one(number:int)->int:
    return number+1

if __name__ == '__main__':
    res=asyncio.run(coroutine_add_one(10))
    print(res)
"""
11
"""
```
`asyncio.run` 首先创建了一个全新的事件。
一旦创建成功，就会接受传递给它的任何协程，运行直到完成，关闭，结束事件循环
## await 关键字暂停执行
```python
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
```
`await`关键字之后会调用其他协程（更具体第说，是一个被称为awaitable对象 它并不总是协程)
`await`关键字会使用后面的协程运行，直接调用协程会返回一个协程对象。
## 使用sleep
```python
import asyncio
async def hello_world()->str:
    await asyncio.sleep(1)
    return 'hello world'

async def main()->None:
    message=await hello_world()
    print(message)
if __name__ == '__main__':
    asyncio.run(main())
```
await 等待hello_world的执行，等1秒。
## 运行两个协程
```python
import asyncio
from util import delay
async def add_one(number:int)->int:
    return number + 1
async def hello_world()->str:
    await delay(1)
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
```
可以发现两个协程是串行的，而不是并行的
`sleep`的时候，`main`和`hello_world`都暂停了。
不是并行的
# 通过任务并行
​    任务是协程的包装器，它安排协程尽快在事件循环上运行。这种调度和执行以非
阻塞方式发生，这意味着一旦创建一个任务，就可以在任务运行时立即执行其他代码。
这与使用阻塞方式的await关键字形成对比，意味着暂停整个协程，直到await表达式
的结果返回。  
​    可创建任务并安排它们在事件循环上立即运行，这意味着可以大致同时执行多个
任务。当这些任务包装一个长时间运行的操作时，它们所做的任何等待都将同时发生。
为说明这一点，下面创建两个任务并尝试同时运行它们。

## 创建任务
​     创建任务是通过`asyncio.create_task`函数来实现的。当调用这个函数时，给它一个
协程来运行，它会立即返回一个任务对象。一旦有了一个任务对象，就可以把它放在
一个await表达式中，它完成后就会提取返回值。
```python
import asyncio
from util import delay
async def main():
    sleep_three=asyncio.create_task(delay(3))
    print(type(sleep_three))
    result = await sleep_three
    print(result)
if __name__ == '__main__':
    asyncio.run(main())
"""
<class '_asyncio.Task'>
睡3秒
结束睡眠3秒
3
"""
```
类型是`<class '_asyncio.Task'>` 表明于协程不同。

`await` 应用于任务，这将暂停主协程，直到从任务中得到结果

## 同时运行多个任务
```python
import asyncio
from util import delay
async def main():
    sleep_for_three=asyncio.create_task(delay(3))
    sleep_for_again=asyncio.create_task(delay(3))
    sleep_for_once_more=asyncio.create_task(delay(3))
    print("______________")
    await sleep_for_three
    await sleep_for_again
    await sleep_for_once_more

if __name__ == '__main__':
    asyncio.run(main())

```
启动了三个任务，每个任务需要3秒，并将同时执行所有的休眠操作。
程序将在三秒左右完成。运行如下
![](asset/PixPin_2025-05-24_22-52-18.png)
## 等待中执行其他代码
```python
import asyncio
from util import delay
async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")

async def main():
    first_delay=asyncio.create_task(delay(3))
    second_delay=asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay

if __name__ == '__main__':
    asyncio.run(main())
"""
睡3秒
睡3秒
I'm running other code while I'm waiting!
I'm running other code while I'm waiting!
结束睡眠3秒
结束睡眠3秒
"""
```
首先启动两个任务，每个任务休眠3秒。然后，当两个任务空闲时，可以看到没秒都输出了
"I'm running other code while I'm waiting!",意味着。即使在运行时间密集型 操作时，应用程序可以执行其他任务。

