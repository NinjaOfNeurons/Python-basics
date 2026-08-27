import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch the data" )
    await asyncio.sleep(sleep_time) 
    return {"data":f"some data from coroutin {id}","id": id } 


async def main():
    task1 = asyncio.create_task(fetch_data(1,2))
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,1))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1,result2,result3)

# Run the main coroutine 
asyncio.run(main())   



#key takes 

#create_task to create tsak 
#evnt loop yahan mst kaam kr raha h abb koi bhi task agr waiting pr h or agr dekha jae to is code to chlne me kull 5 sec lagne chide ne but sare atsk nu await krwa k asi even loop anaal durse atk de waiting time ch koi hor task execute kr sktde han 