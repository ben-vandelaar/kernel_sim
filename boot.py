import asyncio
from kernel import Kernel


async def my_process():
    for i in range(5):
        print(f"[Process] Tick {i}")
        await asyncio.sleep(0)


async def main():
    k = Kernel()
    k.spawn(my_process())
    await k.run()


asyncio.run(main())
