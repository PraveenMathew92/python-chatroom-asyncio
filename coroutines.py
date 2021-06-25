import asyncio


async def coroutine(caller):
    print(f'entering ${caller}')
    await asyncio.sleep(1)
    print(f'exited {caller}')


"""
asyncio.run takes a coroutine and 

A RuntimeWarning is generated if the coroutine is not awaited 
Eg: coroutine('without_run')
"""

asyncio.run(coroutine('coroutine_call'))

"""
create_task creates a task which runs a coroutine in the event loop
"""


async def task_runner():
    task = asyncio.create_task(coroutine('task_call'))
    await task


asyncio.run(task_runner())

print("""
\t\t\tRunning with gather task
""")


async def gather_runner():
    """
    asyncio.gather takes in a bunch of coroutines and runs them concurrently
    """
    await asyncio.gather(
        (coroutine('gather')),
        (task_runner()))


asyncio.run(gather_runner())
