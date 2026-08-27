import asyncio


async def fetch_data(delay, id):
    print("Fetching data id:", id )
    await asyncio.sleep(delay) #simulating and I/O operation with sleep 
    print("Data fetchede, id:", id)
    return {"data":"some data","id": id } # Return some data 


async def main():
    task1 = fetch_data(2,1)
    task2 = fetch_data(1,2)
    
    result1 = await task1
    print(f"Recive some data",result1)

    result2 = await task2
    print(f"Recive some data",result2)
    

# Run the main coroutine 
asyncio.run(main())   


# the event loop 
#key points await will activate the coroutine and after then it will start executing 
#for run the main coroutin you has to have run it this way asyncio.run(main())   otherwise it will not run 
