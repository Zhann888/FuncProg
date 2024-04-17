#Реализовать библиотеку для работы со стримами данных, поддерживающую асинхронное выполнение операций.

import asyncio

async def map_async(data, func):
    mapped_data = []
    for item in data:
        mapped_item = await func(item)
        mapped_data.append(mapped_item)
    return mapped_data


async def filter_async(data, func):
    filtered_data = []
    for item in data:
        if await func(item):
            filtered_data.append(item)
    return filtered_data


async def reduce_async(data, func, initial):
    res = initial
    for item in data:
        res = await func(res, item)
    return res


async def collect_async(data):
    return data


async def main():
    data = [1, 2, 3, 4, 5]

    async def double(x):
        await asyncio.sleep(1)
        return x * 2

    async def is_even(x):
        await asyncio.sleep(1)
        return x % 2 == 0

    async def sum_up(acc, x):
        await asyncio.sleep(1)
        return acc + x

    doubled_data = await map_async(data, double)
    filtered_data = await filter_async(doubled_data, is_even)
    result = await reduce_async(filtered_data, sum_up, 0)
    collected_data = await collect_async(filtered_data)

    print("Result: ", result)
    print(collected_data)


asyncio.run(main())
