from collections.abc import MutableSequence


class ArrayList(MutableSequence):
    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError(f'Type of capacity must be int, not {type(capacity).__name__}')

        if capacity < 0:
            raise ValueError(f'Incorrect capacity value = {capacity}, must be >= 0')

        self.__items = [None] * capacity
        self.__size = 0

    def __check_index_type_and_value(self, index):
        if not isinstance(index, int):
            raise TypeError(f'Incorrect type of argument "{type(index).__name__}", must be int')

        if index + self.__size < 0 or index >= self.__size:
            raise IndexError(f'Incorrect index value = {index}, must be in {0, self.__size - 1} or {-self.__size, -1}')

    def __getitem__(self, index):
        if isinstance(index, slice):
            slice_range = index.indices(self.__size)
            items = []

            for i in range(*slice_range):
                items.append(self.__items[i])

            return items

        self.__check_index_type_and_value(index)

        if index < 0:
            index += self.__size

        return self.__items[index]

    def __setitem__(self, index, value):
        self.__check_index_type_and_value(index)

        if index < 0:
            index += self.__size

        self.__items[index] = value

    def __delitem__(self, index):
        self.__check_index_type_and_value(index)

        if index < 0:
            index += self.__size

        for i in range(index, self.__size - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

    def ensure_capacity(self, capacity):
        if len(self.__items) >= capacity:
            return

        self.__items += [None] * (capacity - len(self.__items))

    def trim_to_size(self):
        if self.__size < len(self.__items):
            self.__items = self.__items[:self.__size]

    def __increase_capacity(self):
        if len(self.__items) == 0:
            self.__items = [None] * 10
            return

        self.__items += [None] * len(self.__items)

    def __len__(self):
        return self.__size

    def __iter__(self):
        for i in range(self.__size):
            yield self.__items[i]

    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError(f'Incorrect type of argument "{type(index).__name__}", must be int')

        if index < 0 or index > self.__size:
            raise IndexError(f'Incorrect index value = {index}, must be in {0, self.__size}')

        if self.__size >= len(self.__items):
            self.__increase_capacity()

        for i in range(self.__size, index, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[index] = value
        self.__size += 1

    def append(self, value):
        if self.__size >= len(self.__items):
            self.__increase_capacity()

        self.__items[self.__size] = value
        self.__size += 1

    def extend(self, other):
        try:
            iter(other)
        except TypeError:
            raise TypeError(f'{type(other).__name__} object is not iterable')

        self.ensure_capacity(self.__size + len(other))

        for i in range(self.__size, self.__size + len(other)):
            self.__items[i] = other[i - self.__size]

        self.__size += len(other)

    def pop(self, index=None):
        if index is None:
            if self.__size == 0:
                raise IndexError('Pop from empty list')

            item = self.__items[self.__size - 1]
            self.__items[self.__size - 1] = None
            self.__size -= 1

            return item

        self.__check_index_type_and_value(index)

        item = self.__items[index]

        for i in range(index, self.__size - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

        return item

    def remove(self, value):
        for i in range(self.__size):
            if self.__items[i] == value:
                self.pop(i)

                return

        raise ValueError('No value in list')

    def __iadd__(self, values):
        if not isinstance(values, ArrayList):
            raise TypeError(f'Incorrect type of argument "{type(values).__name__}", need {self.__class__.__name__}')

        self.extend(list(values))

        return self

    def __contains__(self, value):
        for i in range(self.__size):
            if self.__items[i] == value:
                return True

        return False

    def __reversed__(self):
        for i in range(self.__size - 1, -1, -1):
            yield self.__items[i]

    def index(self, item, start=None, stop=None):
        if start is None:
            start = 0

        if stop is None:
            stop = self.__size - 1

        if start < 0 and stop < 0:
            start += self.__size
            stop += self.__size

        self.__check_index_type_and_value(start)
        self.__check_index_type_and_value(stop)

        for i in range(start, stop):
            if self.__items[i] == item:
                return i

        raise ValueError('Value not found')

    def count(self, value):
        count = 0

        for i in range(self.__size):
            if self.__items[i] == value:
                count += 1

        return count

    def reverse(self):
        for i in range(self.__size // 2):
            self.__items[i], self.__items[self.__size - 1 - i] = self.__items[self.__size - 1 - i], self.__items[i]

    def __repr__(self):
        array_list = []

        if len(self.__items) == 0:
            return str(array_list)

        for i in range(self.__size):
            array_list.append(self.__items[i])

        return str(array_list)
