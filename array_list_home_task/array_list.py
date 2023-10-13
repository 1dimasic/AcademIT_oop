from typing import Any


class ArrayList:
    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError(f'Type of capacity must be int, not {type(capacity).__name__}')

        if capacity < 0:
            raise ValueError(f'Capacity must be >= 0, not {capacity}')

        self.__items: list[Any] = [None] * capacity
        self.__size = 0

    def __len__(self):
        return self.__size

    def __increase_capacity(self):
        if len(self.__items) == 0:
            self.__items = [None] * 10

        self.__items += [None] * len(self.__items)

    def append(self, value):
        if self.__size >= len(self.__items):
            self.__increase_capacity()

        self.__items[self.__size] = value
        self.__size += 1

    def load_from_file(self, path):
        with open(path, 'r') as file:
            for line in file:
                items = line.split(',')

                for i in range(len(items)):
                    self.append(int(items[i]))

    def remove_even_numbers(self):
        for i in range(self.__size):
            if self.__items[i] is None:
                continue

            if self.__items[i] % 2 == 0:
                self.__items[i] = None

    def remove_repetitions(self):
        unique_list = ArrayList(self.__size)

        for i in range(self.__size):
            if self.__items[i] not in unique_list:
                unique_list.append(self.__items[i])

        return unique_list

    def __contains__(self, value):
        for i in range(self.__size):
            if self.__items[i] == value:
                return True

        return False

    def __repr__(self):
        array_list = []

        if len(self.__items) == 0:
            return str(array_list)

        for i in range(self.__size):
            array_list.append(self.__items[i])

        return str(array_list)
