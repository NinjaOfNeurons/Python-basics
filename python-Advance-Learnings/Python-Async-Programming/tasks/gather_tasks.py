import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch the data" )
    await asyncio.sleep(sleep_time) 
    return {"data":f"some data from coroutin {id}","id": id } 


async def main():
    #gather  function  run coroutines concurrently and gather their return values 
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

    for result in results:
        print(f"Received result:{result}")


# Run the main coroutine 
asyncio.run(main())   



# key takes
#gather  function  run coroutines concurrently and gather their return values 
#error handling me acha nhi h gather fucntion 
# aur ye autimatically cancle nhi krega baki coroutine ko agr koi fail hoti h 

