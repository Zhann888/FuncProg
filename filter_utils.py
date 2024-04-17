async def filter_async(data, func):
    filtered_data = []
    for item in data:
        if await func(item):
            filtered_data.append(item)
    return filtered_data