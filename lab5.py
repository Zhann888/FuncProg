# 13.  Создать серию взаимосвязанных ленивых функций, каждая из которых выполняет одно действие в цепочке обработки данных.

def square(num):
    for x in num:
        yield x * x


def sum(num):
    total = 0
    for x in num:
        total += x
    yield total


# data = square(range(1, 6))

data = [9, 2, 3, 4, 5]
# print(next(data))
# print(next(data))
print(next(square(data)))
print(next(square(data)))

# squared_numbers = square(data)
# result = next(sum(squared_numbers))


