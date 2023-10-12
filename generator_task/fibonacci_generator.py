def fibonacci_generator(numbers_count):
    try:
        numbers_count = int(numbers_count)
    except ValueError:
        raise ValueError(f'Invalid literal for int() with base 10: "{numbers_count}"')

    if numbers_count < 0:
        raise ValueError(f'Fibonacci numbers count must be >= 0, not {numbers_count}')

    previous_fibonacci_number = 0
    current_fibonacci_number = 1
    i = 1

    while i <= numbers_count:
        yield previous_fibonacci_number
        previous_fibonacci_number, current_fibonacci_number = \
            current_fibonacci_number, previous_fibonacci_number + current_fibonacci_number

        i += 1


fibonacci_numbers_count = input('Input Fibonacci numbers count: ')
print('Fibonacci numerical series: ', end=' ')
for fibonacci_number in fibonacci_generator(fibonacci_numbers_count):
    print(fibonacci_number, end=' ')
