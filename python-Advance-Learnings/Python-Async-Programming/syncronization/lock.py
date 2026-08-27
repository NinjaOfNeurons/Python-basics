import asyncio

# A Shared variable 
shared_resource = 0



# An asyncio lock
lock = asyncio.Lock()



async def modify_shared_resource():
    global shared_resource
    async with lock:
        #critical session start
        print(f"Resource before modification: {shared_resource}")
        shared_resource +=1  #modify the shared resource
        await asyncio.sleep(1)
        print(f"Resource after modification : {shared_resource}")



async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5) ))


asyncio.run(main())






#jdon tk lock release nhi hunda odon tk koi hor task execulte nhi hoega 