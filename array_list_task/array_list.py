from collections.abc import MutableSequence


class ArrayList(MutableSequence):
    def __init__(self, capacity=10):
        self.items = [None] * capacity
        self.size = 0

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError

        if item < 0 or item > self.size - 1:
            raise IndexError

        return self.items[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError

        if key < 0 or key > self.size - 1:
            raise IndexError

        self.items[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        if key < 0 or key > self.size - 1:
            raise IndexError

        self.pop(key)

    def __ensure_capacity(self, size):
        if len(self.items) >= size:
            return

        self.items = self.items + [None] * (size - len(self.items))

    def __trim_to_size(self):
        if self.size < len(self.items):
            self.items = self.items[:self.size]

    def __increase_capacity(self):
        self.items = self.items + [None] * len(self.items)

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(self.size):
            yield self.items[i]

    def insert(self, key, value):
        if not isinstance(key, int):
            raise TypeError

        if key < 0 or key > self.size - 1:
            raise ValueError

        if self.size >= len(self.items):
            self.__increase_capacity()

        for i in range(self.size, index - 1, -1):
            self.items[i] = self.items[i - 1]

        self.items[key] = value
        self.size += 1

    def append(self, element):
        if self.size >= len(self.items):
            self.__increase_capacity()

        self.items[self.size] = element
        self.size += 1

    def extend(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError

        self.__ensure_capacity(self.size + other.size)

        for i in range(self.size, self.size + other.size):
            self.items[i] = other.items[i - self.size]

        self.size += other.size

    def pop(self, index=None):
        if index is None:
            self.items[self.size - 1] = None
            self.size -= 1
            return

        if index < 0 or index > self.size - 1:
            raise IndexError

        value = self.items[index]
        for i in range(index, self.size - 1):
            self.items[i] = self.items[i + 1]

        self.items[self.size - 1] = None
        self.size -= 1

        return value

    def remove(self, value):
        for i in range(self.size):
            if self.items[i] == value:
                self.pop(i)
                return

        raise ValueError

    def __iadd__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError

        size = self.size + other.size
        self.__ensure_capacity(size)

        for i in range(self.size, size):
            self.items[i] = other.items[i - self.size]

        self.size += other.size

        return self

    def __contains__(self, item):
        return item in self.items

    def __reversed__(self):
        for i in range(self.size - 1, -1, -1):
            yield self.items[i]

    def index(self, value, *searching_range):
        if len(searching_range) == 2:
            if all(isinstance(_, int) for _ in searching_range):
                if all(0 <= _ <= self.size - 1 for _ in searching_range):
                    if searching_range[0] > searching_range[1]:
                        searching_range = searching_range[::-1]

                    for i in range(searching_range[0], searching_range[1]):
                        if self.items[i] == value:
                            return i

                    raise ValueError

                raise IndexError

            raise TypeError

        if len(searching_range) == 1:
            if isinstance(searching_range[0], int):
                if 0 <= searching_range[0] <= self.size - 1:
                    for i in range(searching_range[0], self.size):
                        if self.items[i] == value:
                            return i

                    raise ValueError

                raise IndexError

            raise TypeError

        for i in range(self.size):
            if self.items[i] == value:
                return i

        raise ValueError

    def count(self, element):
        if not element:
            raise ValueError

        count = 0
        for i in range(self.size):
            if self.items[i] == element:
                count += 1

        return count

    def reverse(self):
        for i in range(self.size // 2):
            self.items[i], self.items[self.size - 1 - i] = self.items[self.size - 1 - i], self.items[i]


a = ArrayList(3)
a.append(5)
a.append(8)
a.append(-3)
a.append(0)
b = ArrayList(2)
b.append(6)
b.append(7)
print(a.__delitem__(1))
print(a.items)

