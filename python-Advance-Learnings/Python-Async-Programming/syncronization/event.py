import asyncio

async def waiter(event):
    print("Waiting for event...")
    await event.wait()
    print("Event received! Continuing work.")

async def setter(event):
    await asyncio.sleep(3)
    print("Setting the event")
    event.set()

async def main():
    event = asyncio.Event()

    asyncio.create_task(waiter(event))
    await setter(event)

asyncio.run(main())


# Key Takeaway

# event.wait() blocks until signal is sent

# event.set() wakes all waiting tasks

# No data is passed, only a signal