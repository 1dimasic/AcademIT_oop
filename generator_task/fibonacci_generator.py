def fibonacci_generator(count):
    try:
        count = int(count)
    except ValueError:
        raise ValueError(f'Invalid literal for int() with base 10: "{count}"')

    if count < 0:
        raise ValueError(f'Fibonacci numbers count must be >= 0, not {count}')

    previous_fibonacci_number = 0
    current_fibonacci_number = 1
    i = 1

    while i <= count:
        yield previous_fibonacci_number
        previous_fibonacci_number, current_fibonacci_number = \
            current_fibonacci_number, previous_fibonacci_number + current_fibonacci_number

        i += 1


fibonacci_numbers_count = input('Input Fibonacci numbers count: ')
print('Ряд Фибоначчи:', end=' ')
for fibonacci_number in fibonacci_generator(fibonacci_numbers_count):
    print(fibonacci_number, end=' ')
