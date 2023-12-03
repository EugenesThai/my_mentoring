# asyncio_task 2
import asyncio


async def async_function_1():
    print("Function 1: Start")
    await asyncio.sleep(1)
    print("Function 1: End")


async def async_function_2():
    print("Function 2: Start")
    await asyncio.sleep(2)
    print("Function 2: End")


async def async_function_3():
    print("Function 3: Start")
    await asyncio.sleep(3)
    print("Function 3: End")


async def async_task2():
    results = await asyncio.gather(
        async_function_1(), async_function_2(), async_function_3()
    )


asyncio.run(async_task2())
# Output:
# Function 1: Start
# Function 2: Start
# Function 3: Start
# Function 1: End
# Function 2: End
# Function 3: End
