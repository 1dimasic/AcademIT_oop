import math


class Vector:
    def __init__(self, *args):
        if len(args) > 2 or len(args) == 0:
            raise ValueError(f'Invalid number of arguments = {len(args)}')

        if len(args) == 1:
            if isinstance(args[0], int):
                size = args[0]

                if size <= 0:
                    raise ValueError(f'Size of the vector must be > 0, not {size}')

                self.__components = [0] * size

                return

            if isinstance(args[0], list):
                if len(args[0]) == 0:
                    raise ValueError(f'Size of the vector must be > 0, not {len(args[0])}')

                if not all(isinstance(component, int | float) for component in args[0]):
                    raise ValueError(f'Vector components must be numbers')

                self.__components = args[0][:]

                return

            if isinstance(args[0], Vector):
                vector = args[0]
                self.__components = vector.__components[:]

                return

        size = args[0]

        if not isinstance(size, int):
            raise TypeError(f'Incorrect type of arguments "{type(size).__name__}"')

        if size <= 0:
            raise ValueError(f'Size of the vector must be > 0, not {size}')

        if not isinstance(args[1], list):
            raise TypeError(f'Incorrect type of arguments "{type(size).__name__}"')

        if not all(isinstance(component, int | float) for component in args[1]):
            raise ValueError(f'Vector components must be numbers')

        self.__components = args[1][:]

        if size > len(self.__components):
            self.__components.extend([0] * (size - len(self.__components)))

    def __repr__(self):
        return '{%s}' % ', '.join(map(str, self.__components))

    @property
    def size(self):
        return len(self.__components)

    @property
    def length(self):
        return math.sqrt(sum(map(lambda x: x * x, self.__components)))

    def __increase_size(self, other):
        if self.size < other.size:
            self.__components.extend((other.size - self.size) * [0])

    def __iter__(self):
        for component in self.__components:
            yield component

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        self.__increase_size(other)

        for i in range(other.size):
            self.__components[i] += other.__components[i]

        return self

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        self.__increase_size(other)

        for i in range(other.size):
            self.__components[i] -= other.__components[i]

        return self

    def __imul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        for i in range(self.size):
            self.__components[i] *= other

        return self

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        vectors_sum = Vector(self)
        vectors_sum += other

        return vectors_sum

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        difference = Vector(self)
        difference -= other

        return difference

    def __mul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        product = Vector(self)
        product *= other

        return product

    __rmul__ = __mul__

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError(f'Index must be int, not {type(item).__name__}')

        if item < 0 or item >= self.size:
            raise IndexError(f'Incorrect index value, must be in ({0, self.size - 1})')

        return self.__components[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError(f'Index must be int, not {type(item).__name__}')

        if key < 0 or key >= self.size:
            raise IndexError(f'Incorrect index value, must be in ({0, self.size - 1})')

        if not isinstance(value, int | float):
            raise TypeError('Vector component must be a number')

        self.__components[key] = value

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.size == other.size and self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    def get_scalar_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        product = 0

        for component_1, component_2 in zip(self.__components, other.__components):
            product += component_1 * component_2

        return product
