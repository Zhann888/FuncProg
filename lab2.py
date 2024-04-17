def transform_data(data):
    return dict(map(lambda var: (var[0].upper(), var[1]), data.items()))


original_dict = {
    'one': 1,
    'two': 2,
    'three': 3
}

result = transform_data(original_dict)

print(original_dict)
print(result)
