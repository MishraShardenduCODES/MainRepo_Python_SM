import asyncio

async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
asyncio.run(main())
async def my_coroutine():
    result = await some_async_function()
    print(result)


async def my_coroutine():
    print("Task is running")
    await asyncio.sleep(1)
    print("Task completed")
asyncio.run(my_coroutine())


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")


async def coroutine1():
    await asyncio.sleep(1)
    return "One"
async def coroutine2():
    await asyncio.sleep(2)
    return "Two"
results = asyncio.run(asyncio.gather(coroutine1(), coroutine2()))
print(results)  # Output: ['One', 'Two']



async def my_coroutine(lock):
    async with lock:
        print("Acquired the lock")
        await asyncio.sleep(1)
    print("Released the lock")
asyncio.run(my_coroutine(asyncio.Lock()))


