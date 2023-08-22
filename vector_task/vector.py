import math


class Vector:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError('Invalid number of arguments > 2')

        if len(args) == 2:
            if isinstance(args[0], int):
                if args[0] < 0:
                    raise ValueError('Size of the vector must be > 0')

                if isinstance(args[1], list):
                    self.__components = args[1][:]

                    if args[0] > len(args[1]):
                        self.__components.extend([0] * (args[0] - len(args[1])))

                    return

                raise TypeError(f'Incorrect type of arguments "{type(args[1]).__name__}"')

            raise TypeError(f'Incorrect type of arguments "{type(args[0]).__name__}"')

        if len(args) == 1:
            if isinstance(args[0], int):
                if args[0] > 0:
                    self.__components = [0] * args[0]

                    return

                raise ValueError('Size of the vector must be > 0')

            if isinstance(args[0], list):
                self.__components = args[0][:]

                return

            if isinstance(args[0], Vector):
                self.__components = args[0].__components[:]

                return

            raise TypeError(f'Incorrect type of argument "{type(args[0]).__name__}"')

        raise ValueError('Invalid number of arguments 0')

    def __repr__(self):
        return '{%s}' % ', '.join(map(str, self.__components))

    @property
    def size(self):
        return len(self.__components)

    @property
    def length(self):
        return math.sqrt(sum(list(map(lambda x: x ** 2, self.__components))))

    @property
    def components(self):
        return self.__components

    def __raise_size(self, other):
        if self.size < other.size:
            self.__components.extend((other.size - self.size) * [0])

    def __len__(self):
        return len(self.__components)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        self.__raise_size(other)

        for i in range(other.size):
            self.__components[i] = self.__components[i] + other.__components[i]

        return self

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        self.__raise_size(other)

        for i in range(other.size):
            self.__components[i] = self.__components[i] - other.__components[i]

        return self

    # def __imul__(self, other):
    #     if not isinstance(other, Vector):
    #         raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')
    #
    #     product = 0
    #
    #     for component_1, component_2 in zip(self.__components, other.__components):
    #         product += component_1 * component_2
    #
    #     return product

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        self.__raise_size(other)
        component = [0] * self.size

        for i in range(other.size):
            component[i] = self.__components[i] + other.__components[i]

        for j in range(other.size, self.size):
            component[j] = self.__components[j]

        return Vector(component)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        self.__raise_size(other)
        component = [0] * self.size

        for i in range(other.size):
            component[i] = self.__components[i] - other.__components[i]

        for j in range(other.size, self.size):
            component[j] = self.__components[j]

        return Vector(component)

    def __mul__(self, other):
        product = 0

        for component_1, component_2 in zip(self.__components, other.__components):
            product += component_1 * component_2

        return product

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Index must be int')

        if item < 0 or item >= self.size:
            raise IndexError(f'Incorrect index value, must be in ({0, self.size - 1})')

        return self.__components[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Index must be int')

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

    def multiply_by_scalar(self, other):
        if not isinstance(other, int | float):
            raise TypeError

        for i in range(self.size):
            self.__components[i] *= other

        return self
