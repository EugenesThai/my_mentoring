# asyncio_task 1

import asyncio


async def main():
    print(1)
    await asyncio.sleep(2)
    print(2)
    print(3)


asyncio.run(main())

# Output: 1 - (sleep for 2 sec) - 2 - 3
