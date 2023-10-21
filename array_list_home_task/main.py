def get_strings_list_from_file():
    try:
        with open('list.dat', 'r') as file:
            items = []

            for line in file:
                items.append(line)

    except FileNotFoundError:
        pass

    return items


def remove_even_numbers(numbers_list):
    i = 0

    while i < len(numbers_list):
        if numbers_list[i] % 2 == 0:
            for j in range(i, len(numbers_list) - 1):
                numbers_list[j] = numbers_list[j + 1]

            del numbers_list[-1]

        i += 1


def get_list_without_repetitions(numbers_list):
    unique_elements_list = []

    for number in numbers_list:
        if number not in unique_elements_list:
            unique_elements_list.append(number)

    return unique_elements_list


print(f'Strings list: {get_strings_list_from_file()}')

values_list = [1, 2, 3, 4, 5, 6, 7]
remove_even_numbers(values_list)
print(f'Without even numbers list: {values_list}')

values_list = [1, 2, 1, 1, 4, 7, 6, 7, 6, 10]
values_list_without_repetitions = get_list_without_repetitions(values_list)
print(f'Without repetitions list: {values_list_without_repetitions}')
