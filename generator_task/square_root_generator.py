import math


def square_root_generator(numbers_count):
    try:
        numbers_count = int(numbers_count)
    except ValueError:
        raise ValueError(f'Invalid literal for int() with base 10: "{numbers_count}"')

    if numbers_count < 0:
        raise ValueError(f'Numbers count must be >= 0, not {numbers_count}')

    for i in range(numbers_count):
        yield math.sqrt(i)


series_numbers_count = input('Input numerical series of square root numbers count: ')
print('Numerical series:', end=' ')
for number_square_root in square_root_generator(series_numbers_count):
    print('%.3f' % number_square_root, end=' ')
