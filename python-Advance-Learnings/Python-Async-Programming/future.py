import asyncio

async def producer(future):
    await asyncio.sleep(2)
    future.set_result("Data is ready!")

async def consumer(future):
    print("Consumer waiting for result...")
    result = await future
    print("Consumer got:", result)

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(producer(future))
    await consumer(future)

asyncio.run(main())



# Key Takeaway

# future starts empty

# await future waits

# set_result() completes the future