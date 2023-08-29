from collections.abc import MutableSequence


class ArrayList(MutableSequence):
    def __init__(self, capacity=10):
        self.__items = [None] * capacity
        self.__size = 0

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError(f'Incorrect type of argument "{type(item).__name__}"')

        if item < 0 or item > self.__size - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1})')

        return self.__items[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        if key < 0 or key > self.__size - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1})')

        self.__items[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        if key < 0 or key > self.__size - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1})')

        self.pop(key)

    def __ensure_capacity(self, size):
        if len(self.__items) >= size:
            return

        self.__items = self.__items + [None] * (size - len(self.__items))

    def __trim_to_size(self):
        if self.__size < len(self.__items):
            self.__items = self.__items[:self.__size]

    def __increase_capacity(self):
        self.__items = self.__items + [None] * len(self.__items)

    def __len__(self):
        return self.__size

    def __iter__(self):
        for i in range(self.__size):
            yield self.__items[i]

    def insert(self, key, value):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        if key < 0 or key > self.__size:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__size})')

        if self.__size >= len(self.__items):
            self.__increase_capacity()

        if key == self.__size:
            self.__items[key] = value
            self.__size += 1

            return

        for i in range(self.__size, key - 1, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[key] = value

    def append(self, value):
        if self.__size >= len(self.__items):
            self.__increase_capacity()

        self.__items[self.__size] = value
        self.__size += 1

    def extend(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        self.__ensure_capacity(self.__size + other.__size)

        for i in range(self.__size, self.__size + other.__size):
            self.__items[i] = other.__items[i - self.__size]

        self.__size += other.__size

    def pop(self, index=None):
        if index is None:
            self.__items[self.__size - 1] = None
            self.__size -= 1
            return

        if not isinstance(index, int):
            raise TypeError(f'Incorrect type of argument "{type(index).__name__}"')

        if index < 0 or index > self.__size - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1})')

        value = self.__items[index]
        for i in range(index, self.__size - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

        return value

    def remove(self, value):
        for i in range(self.__size):
            if self.__items[i] == value:
                self.pop(i)
                return

        raise ValueError(f'No value in list')

    def __iadd__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        size = self.__size + other.__size
        self.__ensure_capacity(size)

        for i in range(self.__size, size):
            self.__items[i] = other.__items[i - self.__size]

        self.__size += other.__size

        return self

    def __contains__(self, item):
        return item in self.__items

    def __reversed__(self):
        for i in range(self.__size - 1, -1, -1):
            yield self.__items[i]

    def index(self, value, *searching_range):
        if len(searching_range) == 2:
            if all(isinstance(_, int) for _ in searching_range):
                if all(0 <= _ <= self.__size - 1 for _ in searching_range):
                    if searching_range[0] > searching_range[1]:
                        searching_range = searching_range[::-1]

                    for i in range(searching_range[0], searching_range[1]):
                        if self.__items[i] == value:
                            return i

                    raise ValueError(f'No value in list')

                raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1})')

            raise TypeError(f'Incorrect type of argument "{type(searching_range[0]).__name__} or '
                            f'{type(searching_range[1]).__name__}"')

        if len(searching_range) == 1:
            if isinstance(searching_range[0], int):
                if 0 <= searching_range[0] <= self.__size - 1:
                    for i in range(searching_range[0], self.__size):
                        if self.__items[i] == value:
                            return i

                    raise ValueError(f'No value in list')

                raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1})')

            raise TypeError(f'Incorrect type of argument "{type(searching_range[0]).__name__}')

        if len(searching_range) == 0:
            for i in range(self.__size):
                if self.__items[i] == value:
                    return i

            raise ValueError(f'No value in list')

        raise ValueError('Invalid number of arguments')

    def count(self, value):
        if not value:
            raise ValueError('Invalid number of arguments')

        count = 0
        for i in range(self.__size):
            if self.__items[i] == value:
                count += 1

        return count

    def reverse(self):
        for i in range(self.__size // 2):
            self.__items[i], self.__items[self.__size - 1 - i] = self.__items[self.__size - 1 - i], self.__items[i]

    def __repr__(self):
        string = ''
        for i in range(len(self.__items)):
            string += str(self.__items[i]) + ' '

        return string
