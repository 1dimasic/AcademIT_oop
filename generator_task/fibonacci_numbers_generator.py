def get_fibonacci_numbers(numbers_count):
    if not isinstance(numbers_count, int):
        raise TypeError(f'Invalid type of argument = {type(numbers_count).__name__}, must be int')

    if numbers_count < 0:
        raise ValueError(f'Invalid numbers count = {numbers_count}, must be >= 0')

    previous_fibonacci_number = 0
    current_fibonacci_number = 1
    i = 1

    while i <= numbers_count:
        yield previous_fibonacci_number
        previous_fibonacci_number, current_fibonacci_number = \
            current_fibonacci_number, previous_fibonacci_number + current_fibonacci_number

        i += 1


fibonacci_numbers_count = int(input('Input Fibonacci numbers count: '))
print('Fibonacci numerical series:', end=' ')

for fibonacci_number in get_fibonacci_numbers(fibonacci_numbers_count):
    print(fibonacci_number, end=' ')
