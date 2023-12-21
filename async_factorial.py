import asyncio

async def facto(a) :
    if a <= 1 :
        return a
    else :
        return await facto(a-1) * a

async def main() :
     a = int(input("Tell a number : "))
     result = await facto(a)
     print(f"The factorial of {a} is {result}")

asyncio.run(main())