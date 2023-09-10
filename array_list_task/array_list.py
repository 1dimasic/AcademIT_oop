from collections.abc import MutableSequence


class ArrayList(MutableSequence):
    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError(f'can not multiply sequence by non-int of type {type(capacity)}')

        if capacity <= 0:
            raise IndexError('list assignment index out of range')

        self.__items = [None] * capacity
        self.__size = 0

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError(f'Incorrect type of argument "{type(item).__name__}"')

        if item < 0 or item >= self.__size:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__size - 1}), not {item}')

        return self.__items[item]

    def __setitem__(self, key, item):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        if key < 0 or key >= self.__size:
            raise IndexError(f'Incorrect index, must be in ({0, self.__size - 1}), not {key}')

        self.__items[key] = item

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        if key < 0 or key >= self.__size:
            raise IndexError(f'Incorrect index, must be in ({0, self.__size - 1}), not {key}')

        for i in range(key, self.__size - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

    def ensure_capacity(self, size):
        if len(self.__items) >= size:
            return

        self.__items = self.__items + [None] * (size - len(self.__items))

    def trim_to_size(self):
        if self.__size < len(self.__items):
            self.__items = self.__items[:self.__size]

    def increase_capacity(self):
        self.__items = self.__items + [None] * len(self.__items)

    def __len__(self):
        return self.__size

    def __iter__(self):
        for item in self.__items:
            yield item

    def insert(self, key, item):
        if not isinstance(key, int):
            raise TypeError(f"Incorrect type of argument '{type(key).__name__}', not 'int'")

        if key < 0 or key > self.__size:
            raise IndexError(f'Incorrect index, must be in ({0, self.__size})')

        if self.__size >= len(self.__items):
            self.increase_capacity()

        if key == self.__size:
            self.__items[key] = item
            self.__size += 1

            return

        for i in range(self.__size, key - 1, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[key] = item
        self.__size += 1

    def append(self, item):
        if self.__size >= len(self.__items):
            self.increase_capacity()

        self.__items[self.__size] = item
        self.__size += 1

    def extend(self, other):
        if not iter(other):
            raise TypeError(f'{type(other)} object is not iterable')

        self.ensure_capacity(self.__size + len(other))

        for i in range(self.__size, self.__size + len(other)):
            self.__items[i] = other[i - self.__size]

        self.__size += len(other)

    def pop(self, index=None):
        if index is None:
            if self.__size == 0:
                raise IndexError('pop from empty list')

            item = self.__items[self.__size - 1]
            self.__items[self.__size - 1] = None
            self.__size -= 1

            return item

        if not isinstance(index, int):
            raise TypeError(f"Incorrect type of argument '{type(index).__name__}', not 'int'")

        if index < 0 or index >= self.__size:
            raise IndexError(f'Incorrect index, must be in {0, self.__size - 1}, not {index}')

        item = self.__items[index]

        for i in range(index, self.__size - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

        return item

    def remove(self, item):
        for i in range(self.__size):
            if self.__items[i] == item:
                self.pop(i)

                return

        raise ValueError(f'No item in list')

    def __iadd__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}", need {self.__class__.__name__}')

        self.extend(other)

        return self

    def __contains__(self, item):
        for i in range(self.__size):
            if self.__items[i] == item:
                return True

        return False

    def __reversed__(self):
        for i in range(self.__size - 1, -1, -1):
            yield self.__items[i]

    def __check_searching_range(self, *searching_range):
        for point in searching_range:
            if not point:
                continue

            if not isinstance(point, int):
                raise TypeError(f'Incorrect type of argument {type(point).__name__}')

            if not 0 <= point < self.__size:
                raise IndexError(f'Incorrect index, must be in ({0, self.__size - 1}), not {point}')

    def index(self, item, *searching_range):
        check = True

        try:
            start = searching_range[0]
        except IndexError:
            start = 0
            check = not check

        try:
            stop = searching_range[1]
        except IndexError:
            stop = self.__size - 1
            check = not check

        if not check:
            self.__check_searching_range(start, stop)

            if start > stop:
                start, stop = stop, start

        for i in range(start, stop + 1):
            if self.__items[i] == item:
                return i

        raise ValueError('item not found')

    def count(self, item=None):
        count = 0

        for i in range(self.__size):
            if self.__items[i] == item:
                count += 1

        return count

    def reverse(self):
        for i in range(self.__size // 2):
            self.__items[i], self.__items[self.__size - 1 - i] = self.__items[self.__size - 1 - i], self.__items[i]

    def __repr__(self):
        string = '['

        for i in range(len(self.__items) - 1):
            string += str(self.__items[i]) + ', '

        string += str(self.__items[len(self.__items) - 1]) + ']'

        return string
