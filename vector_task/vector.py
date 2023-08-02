import math


class Vector:
    def __init__(self, constructor=None, components=None):
        if isinstance(constructor, int):
            if constructor <= 0:
                raise ValueError('Vector dimension must be greater than zero')
            else:
                if components is None:
                    components = constructor * [0]
                else:
                    if constructor > len(components):
                        components.extend((constructor - len(components)) * [0])

                self.__components = components

        if isinstance(constructor, Vector):
            self.__components = constructor.__components.copy()

        if isinstance(constructor, list):
            self.__components = constructor.copy()

    def __repr__(self):
        return '{%s}' % ', '.join(map(str, self.__components))

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, components):
        if not isinstance(components, list):
            raise TypeError('Vector components must be stored in a list')

        for component in components:
            if not isinstance(component, int | float):
                raise TypeError('Vector component must be a number')

        self.__components = components

    @property
    def size(self):
        return len(self.__components)

    @property
    def length(self):
        length = 0

        for component in self.__components:
            length += pow(component, 2)

        return math.sqrt(length)

    def convert_to_one_size(self, other):
        if self.size < other.size:
            self.__components.extend((other.size - self.size) * [0])

            return self

        if self.size > other.size:
            other.__components.extend((self.size - other.size) * [0])

            return other

    def __iadd__(self, other):
        self.convert_to_one_size(other)

        for i in range(self.size):
            self.__components[i] += other.__components[i]

        return self

    def __isub__(self, other):
        self.convert_to_one_size(other)

        for i in range(self.size):
            self.__components[i] -= other.__components[i]

        return self

    def __imul__(self, other):
        for i in range(self.size):
            self.__components[i] *= other

        return self

    def __add__(self, other):
        self.convert_to_one_size(other)

        return Vector([component_1 + component_2 for component_1, component_2 in
                       zip(self.__components, other.__components)])

    def __sub__(self, other):
        self.convert_to_one_size(other)

        return Vector([component_1 - component_2 for component_1, component_2 in
                       zip(self.__components, other.__components)])

    def __mul__(self, other):
        product = 0
        self.convert_to_one_size(other)

        for component_1, component_2 in zip(self.__components, other.__components):
            product += component_1 * component_2

        return product

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Index must be int')

        if item < 0 or item > self.size - 1:
            raise IndexError('Incorrect index value')

        return self.__components[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Index must be int')

        if key < 0 or key > self.size - 1:
            raise IndexError('Incorrect index value')

        if not isinstance(value, int | float):
            raise TypeError('Vector component must be a number')

        self.__components[key] = value

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.size == other.size and self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    def expand(self):
        for i in range(self.size):
            self.__components[i] *= -1

        return self
