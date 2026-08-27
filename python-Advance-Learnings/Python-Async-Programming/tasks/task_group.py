import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch the data" )
    await asyncio.sleep(sleep_time) 
    return {"data":f"some data from coroutin {id}","id": id } 


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i , sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)

    #After the task group block , all tasks have completed
    results =[task.result() for task in tasks]

    for result in results:
        print(f"Recived result:{result}")
    

# Run the main coroutine 
asyncio.run(main())   



