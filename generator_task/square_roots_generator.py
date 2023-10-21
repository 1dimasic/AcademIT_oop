import math


def get_numbers_square_roots(numbers_count):
    if not isinstance(numbers_count, int):
        raise TypeError(f'Invalid type of argument = {type(numbers_count).__name__}, must be int')

    if numbers_count < 0:
        raise ValueError(f'Invalid numbers count = {numbers_count}, must be >= 0')

    for i in range(numbers_count):
        yield math.sqrt(i)


series_numbers_count = int(input('Input numerical series of square root numbers count: '))
print('Numerical series:', end=' ')

for number_square_root in get_numbers_square_roots(series_numbers_count):
    print('%.3f' % number_square_root, end=' ')
