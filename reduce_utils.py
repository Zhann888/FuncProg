async def reduce_async(data, func, initial):
    res = initial
    for item in data:
        res = await func(res, item)
    return res