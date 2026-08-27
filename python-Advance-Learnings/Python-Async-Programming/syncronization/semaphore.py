import asyncio

# A Shared variable 
shared_resource = 0



# An asyncio lock
lock = asyncio.Lock()



async def access_resource(semaphore, resource_id):
    global shared_resource
    async with semaphore:
        #critical session start
        print(f"access resource: {resource_id}")
        await asyncio.sleep(1)
        print(f"Relesing resource : {resource_id}")



async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5) ))


asyncio.run(main())






