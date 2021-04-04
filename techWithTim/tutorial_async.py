import asyncio

# Create a coroutine.
"""
  Is a wrap version of a function the allows 
    to run async.
  
  stop at 15:39
"""
# To use the await keyword, this must be done inside of async function.
# Do not forget the event loop.
# To  execute a coroutine you have to use await.
# Its also mandatory create a event loop.


async def main():
    print("Marcos")
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(0.5)
    print("finish")


async def foo(text):
    print(text)
    await asyncio.sleep(6)  # This thing - the await -  here return a coroutine


asyncio.run(main())  # Star the event loop here
