from collections.abc import Collection
from typing import Any


class HashTable(Collection):
    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError(f'Capacity must have type int, not {type(capacity)}')

        if capacity <= 0:
            raise ValueError(f'Capacity must be > 0, not {capacity}')

        self.__table: list[Any] = [None] * capacity
        self.__size = 0

    def __contains__(self, value):
        index = self.__get_index(value)
        return self.__table[index] and value in self.__table[index]

    def __len__(self):
        return self.__size

    def __iter__(self):
        for items_list in self.__table:
            if items_list is None:
                continue

            for item in items_list:
                yield item

    def __get_index(self, value):
        return abs(hash(value) % len(self.__table))

    def add(self, value):
        index = self.__get_index(value)

        if self.__table[index] is not None:
            self.__table[index].append(value)
        else:
            self.__table[index] = [value]

        self.__size += 1

    def delete(self, value):
        index = self.__get_index(value)

        if self.__table[index] is None:
            return False

        try:
            self.__table[index].remove(value)
            self.__size -= 1
        except ValueError:
            return False

        return True

    def __repr__(self):
        return str(list(self))
