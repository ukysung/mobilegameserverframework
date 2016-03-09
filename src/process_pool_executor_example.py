
import asyncio
import asyncio.futures
import concurrent.futures

process_pool = concurrent.futures.ProcessPoolExecutor(4)

def b(i):
    print(i)

@asyncio.coroutine
def a():
    yield from asyncio.futures.wrap_future(process_pool.submit(b, 1))

next(a())

