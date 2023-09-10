from collections.abc import Collection


class HashTable(Collection):
    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError(f'can not multiply sequence by non-int of type {type(capacity)}')

        if capacity <= 0:
            raise IndexError('list assignment index out of range')

        self.__table = [None] * capacity
        self.__size = 0

    def __contains__(self, value):
        for _ in self.__table:
            if _ is None:
                continue

            for item in _:
                if item == value:
                    return True

        return False

    def __len__(self):
        return self.__size

    def __iter__(self):
        for _ in self.__table:
            if _ is None:
                continue

            for item in _:
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
        else:
            try:
                self.__table[index].remove(value)
            except ValueError:
                pass
            finally:
                self.__size -= 1
                return True

    def __repr__(self):
        hash_table_list = []

        iterator = self.__iter__()

        for items in iterator:
            hash_table_list.append(items)

        return str(hash_table_list)
