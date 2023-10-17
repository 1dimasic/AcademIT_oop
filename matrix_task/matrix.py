from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError(f'Invalid number of arguments = {len(args)}')

        if len(args) == 2:
            rows_count = args[0]
            columns_count = args[1]
            sizes = rows_count, columns_count

            if all(isinstance(size, int) for size in sizes):
                if all(size > 0 for size in sizes):
                    self.__rows = [Vector(columns_count) for _ in range(rows_count)]

                    return

                raise ValueError(f'Sizes of the matrix must be > 0, not {rows_count} or {columns_count}')

            raise TypeError(f'Incorrect type of arguments "{type(rows_count).__name__}" or '
                            f'"{type(columns_count).__name__}", must be int')

        if len(args) == 1:
            if isinstance(args[0], Matrix):
                matrix = args[0]
                self.__rows = matrix.__rows[:][:]

                return

            if isinstance(args[0], list):
                if all(isinstance(vector, Vector) for vector in args[0]):
                    vectors_list = args[0]
                    self.__rows = []
                    max_size = max(vector.size for vector in vectors_list)

                    for i in range(len(vectors_list)):
                        self.__rows.append(Vector(max_size, list(vectors_list[i])))

                    return

                if all(isinstance(vector, list) for vector in args[0]):
                    items = args[0]

                    if all(isinstance(item, int | float) for row in items for item in row):
                        self.__rows = []
                        max_size = len(max(items, key=len))

                        for i in range(len(items)):
                            self.__rows.append(Vector(max_size, items[i]))

                        return

                    raise TypeError('Incorrect type of values in list, must be int or float')

                raise TypeError(f'Incorrect type {type(args[0]).__name__}, must be list')

            raise TypeError(f'Incorrect type of arguments "{type(args[0]).__name__}", must be list')

        raise ValueError('Invalid number of arguments 0')

    @property
    def rows_count(self):
        return len(self.__rows)

    @property
    def columns_count(self):
        return self.__rows[0].size

    def __hash__(self):
        return hash(tuple(tuple(vector) for vector in self.__rows))

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.rows_count != other.rows_count or self.columns_count != other.columns_count:
            return False

        for row_1, row_2 in zip(self.__rows, other.__rows):
            if row_1 != row_2:
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

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f'Index must be int, not {type(index).__name__}')

        if index < 0 or index >= self.rows_count:
            raise IndexError(f'Incorrect index value={index}, must be in {0, self.rows_count - 1}')

        return Vector(self.__rows[index])

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError(f'Index must be int, not {type(index).__name__}')

        if index < 0 or index >= self.rows_count:
            raise IndexError(f'Incorrect index value={index}, must be in {0, self.rows_count - 1}')

        if isinstance(value, list):
            if len(value) != self.columns_count:
                raise ValueError(f'Incorrect vector size = {len(value)}, must be {self.columns_count}')

            self.__rows[index] = Vector(value)

            return

        if isinstance(value, Vector):
            if value.size != self.columns_count:
                raise ValueError(f'Incorrect vector size = {value.size}, must be {self.columns_count}')

            self.__rows[index] = Vector(value)

            return

        raise TypeError('Vector must be a list or class Vector')

    def __mul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}", must be int or float')

        product = Matrix(self)
        product *= other

        return product

    __rmul__ = __mul__

    def __imul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}", must be int or float')

        for i in range(self.rows_count):
            self.__rows[i] *= other

        return self

    def __check_correct_type_and_sizes_equality(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Incorrect type of argument "{type(other).__name__}", must be class Matrix')

        if self.rows_count != other.rows_count or self.columns_count != other.columns_count:
            raise ValueError(
                f'Matrices sizes do not match: ({self.rows_count}x{self.columns_count}), '
                f'({other.rows_count}x{other.columns_count})')

    def __iadd__(self, other):
        self.__check_correct_type_and_sizes_equality(other)

        for i in range(self.rows_count):
            self.__rows[i] += other.__rows[i]

        return self

    def __isub__(self, other):
        self.__check_correct_type_and_sizes_equality(other)

        for i in range(self.rows_count):
            self.__rows[i] -= other.__rows[i]

        return self

    def __add__(self, other):
        self.__check_correct_type_and_sizes_equality(other)

        matrices_sum = Matrix(self)
        matrices_sum += other

        return matrices_sum

    def __sub__(self, other):
        self.__check_correct_type_and_sizes_equality(other)

        matrices_difference = Matrix(self)
        matrices_difference -= other

        return matrices_difference

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            if self.columns_count != other.rows_count:
                raise ValueError(f'Сan not multiply matrix size ({self.rows_count}x{self.columns_count}) '
                                 f'by matrix size ({other.rows_count}x{other.columns_count})')

            product = []

            for i in range(self.rows_count):
                row = []

                for j in range(other.columns_count):
                    item = 0

                    for k in range(self.columns_count):
                        item += self.__rows[i][k] * other.__rows[k][j]

                    row.append(item)

                product.append(row)

            return Matrix(product)

        if isinstance(other, Vector):
            if self.columns_count != other.size:
                raise ValueError(f'Сan not multiply matrix size ({self.rows_count}x{self.columns_count}) '
                                 f'by vector size ({other.size})')

            vector = []

            for i in range(self.rows_count):
                item = 0

                for j in range(other.size):
                    item += self[i][j] * other[j]

                vector.append(item)

            return Vector(vector)

        raise TypeError(f'Incorrect type of argument "{type(other).__name__}", must be class Matrix or class Vector')

    def get_column(self, index):
        if not isinstance(index, int):
            raise TypeError(f'Incorrect type of argument "{type(index).__name__}", must be int')

        if index < 0 or index >= self.columns_count:
            raise IndexError(f'Index column {index} out of range {0, self.columns_count - 1})')

        return Vector([row[index] for row in self.__rows])

    def transpose(self):
        self.__rows = [Vector(list(column)) for column in zip(*self.__rows)]

    def __get_minor(self, i):
        return Matrix([list(vector)[:i] + list(vector)[i + 1:] for vector in self.__rows[1:]])

    def get_determinant(self):
        if self.rows_count != self.columns_count:
            raise ValueError(f'Can not calculate determinant of matrix sizes ({self.rows_count}x{self.columns_count})')

        if self.rows_count == 1:
            return self.__rows[0][0]

        if self.rows_count == 2:
            return self.__rows[0][0] * self.__rows[1][1] - self.__rows[0][1] * self.__rows[1][0]

        determinant = 0

        for i in range(self.rows_count):
            determinant += (-1) ** i * self.__rows[0][i] * self.__get_minor(i).get_determinant()

        return determinant
