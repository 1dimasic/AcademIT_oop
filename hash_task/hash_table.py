from collections.abc import Collection


class HashTable(Collection):
    def __init__(self, capacity=10):
        self.__items = [...] * capacity
        self.__size = 0

    def __contains__(self, item):
        return item in self.__items

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        for i in range(len(self.__items)):
            if self.__items[i] is Ellipsis:
                continue

            for j in range(len(self.__items[i])):
                yield self.__items[i][j]

    def add(self, value):
        index = abs(hash(value) % len(self.__items))
        if self.__items[index] is not Ellipsis:
            self.__items[index].append(value)

        else:
            self.__items[index] = [value]

        self.__size += 1

    def find(self, value):
        index = abs(hash(value) % len(self.__items))
        if self.__items[index] is Ellipsis:
            return None

        for i in range(len(self.__items[index])):
            if self.__items[index][i] == value:
                return index, i

    def __repr__(self):
        hash_table = ''
        for items in self.__items:
            hash_table += str(items) + ' '

        return hash_table
