import asyncio

async def async_function():
    print("Starting async function...")
    await asyncio.sleep(1) # sleep is use for they delay of the time 
    print("Async function completed!")

# Run the async function directly with await
await async_function()
# this code is for jyupiter notebook



#  this code is for pythin file 
# import asyncio

# async def async_function():
#     print("Starting async function...")
#     await asyncio.sleep(1)
#     print("Async function completed!")

# # Example usage
# asyncio.run(async_function())