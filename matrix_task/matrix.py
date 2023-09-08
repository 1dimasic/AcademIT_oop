from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError(f'Invalid number of arguments = {len(args)}')

        if len(args) == 2:
            rows = args[0]
            columns = args[1]
            sizes = rows, columns

            if all(isinstance(size, int) for size in sizes):
                if all(size > 0 for size in sizes):
                    self.__rows = [Vector(columns)] * rows

                    return

                raise ValueError(f'Sizes of the matrix must be > 0, not {rows} or {columns}')

            raise TypeError(f'Incorrect type of arguments "{type(rows).__name__}" or "{type(columns).__name__}"')

        if len(args) == 1:
            if isinstance(args[0], Matrix):
                matrix = args[0]
                self.__rows = matrix.__rows[:][:]

                return

            if isinstance(args[0], list):
                vectors_list = args[0]

                if all(isinstance(vector, Vector) for vector in vectors_list):
                    self.__rows = []
                    max_size = max(vector.size for vector in vectors_list)

                    for i in range(len(vectors_list)):
                        self.__rows.append(Vector(max_size, list(vectors_list[i])))

                    return

                if all(isinstance(vector, list) for vector in vectors_list):
                    if all(isinstance(item, int | float) for vector in vectors_list for item in vector):
                        self.__rows = []
                        max_size = len(max(vectors_list, key=len))

                        for i in range(len(vectors_list)):
                            self.__rows.append(Vector(max_size, vectors_list[i]))

                        return

                    raise TypeError('Incorrect type of values in list')

                raise TypeError('Incorrect type of values in list')

            raise TypeError(f'Incorrect type of arguments "{type(args[0]).__name__}"')

        raise ValueError('Invalid number of arguments 0')

    @property
    def rows(self):
        return len(self.__rows)

    @property
    def columns(self):
        return self.__rows[0].size

    def __hash__(self):
        return hash(tuple(tuple(vector) for vector in self.__rows))

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Incorrect type of arguments "{type(other).__name__}"')

        if self.rows != other.rows or self.columns != other.columns:
            return 'Class instances have different sizes'

        for item_1, item_2 in zip(self.__rows, other.__rows):
            if item_1 != item_2:
                return False

        return True

    def __str__(self):
        return '{%s}' % ', '.join(map(str, self.__rows))

    def __repr__(self):
        matrix = ''
        width = len(str(max(item for row in self.__rows for item in row)))

        for row in self.__rows:
            for item in row:
                matrix += str(item).center(width) + ' '

            matrix += '\n'

        return matrix

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError(f'Index must be int, not {type(item).__name__}')

        if item < 0 or item >= self.rows:
            raise IndexError(f'Incorrect index value, must be in ({0, self.size - 1})')

        return Vector(self.__rows[item])

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError(f'Index must be int, not {type(item).__name__}')

        if key < 0 or key >= self.rows:
            raise IndexError(f'Incorrect index value, must be in ({0, self.size[1] - 1})')

        if isinstance(value, list):
            if len(value) != self.columns:
                raise ValueError(f'Incorrect list size = {len(value)}, must be {self.columns}')

            self.__rows[key] = Vector(value)

            return

        if isinstance(value, Vector):
            if value.size != self.columns:
                raise ValueError(f'Incorrect list size = {value.size}, must be {self.columns}')

            self.__rows[key] = Vector(value)

            return

        raise TypeError('Vector component must be a list or class Vector')

    def __mul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        product = Matrix(self)
        product *= other

        return product

    __rmul__ = __mul__

    def __imul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        for i in range(self.rows):
            self.__rows[i] *= other

        return self

    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        if self.rows != other.rows or self.columns != other.columns:
            return 'Class instances have different sizes'

        for i in range(self.rows):
            self.__rows[i] += other.__rows[i]

        return self

    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        if self.rows != other.rows or self.columns != other.columns:
            return 'Class instances have different sizes'

        for i in range(self.rows):
            self.__rows[i] -= other.__rows[i]

        return self

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        if self.rows != other.rows or self.columns != other.columns:
            return 'Class instances have different sizes'

        amount = Matrix(self)
        amount += other

        return amount

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

        if self.rows != other.rows or self.columns != other.columns:
            return 'Class instances have different sizes'

        difference = Matrix(self)
        difference -= other

        return difference

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.columns or self.columns != other.rows:
                return f'Сan not multiply matrix size ({self.rows}x{self.columns}) ' \
                       f'by matrix size ({other.rows}x{other.columns})'

            product = []

            for i in range(self.rows):
                row = []

                for j in range(self.rows):
                    item = 0

                    for k in range(self.columns):
                        item += self.__rows[i][k] * other.__rows[k][j]

                    row.append(item)

                product.append(row)

            return Matrix(product)

        if isinstance(other, Vector):
            if self.columns != other.size:
                return f'Сan not multiply matrix size ({self.rows},{self.columns}) by vector size ({other.size})'

            vector = []

            for i in range(self.rows):
                item = 0

                for j in range(other.size):
                    item += self[i][j] * other[j]

                vector.append(item)

            return Vector(vector)

        raise TypeError(f'Incorrect type of argument "{type(other).__name__}"')

    def get_column(self, index):
        if not isinstance(index, int):
            raise TypeError(f'Incorrect type of argument "{type(item).__name__}"')

        if index < 0 or index >= self.rows:
            raise IndexError('Index column out of range')

        return Vector([row[index] for row in self.__rows])

    def transpose(self):
        for i in range(self.rows):
            for j in range(i + 1, self.columns):
                self.__rows[i][j], self.__rows[j][i] = self.__rows[j][i], self.__rows[i][j]

    def __get_minor(self, i):
        return Matrix([list(vector)[:i] + list(vector)[i + 1:] for vector in self.__rows[1:]])

    def get_determinant(self):
        if self.rows != self.columns:
            raise ValueError(f'Can not calculate determinant of matrix sizes ({self.rows}x{self.columns})')

        if self.rows == 1:
            return self.__rows[0][0]

        if self.rows == 2:
            return self.__rows[0][0] * self.__rows[1][1] - self.__rows[0][1] * self.__rows[1][0]

        determinant = 0

        for i in range(self.rows):
            determinant += (-1) ** i * self.__rows[0][i] * self.__get_minor(i).get_determinant()

        return determinant
