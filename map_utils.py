async def map_async(data, func):
    mapped_data = []
    for item in data:
        mapped_item = await func(item)
        mapped_data.append(mapped_item)
    return mapped_data
