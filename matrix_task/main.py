from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError('Invalid number of arguments > 2')

        if len(args) == 2:
            if all(isinstance(arg, int) for arg in args):
                if all(arg > 0 for arg in args):
                    self.__matrix = [Vector(args[0])] * args[1]

                    return

                raise ValueError('Sizes of the matrix must be > 0')

            raise TypeError(f'Incorrect type of arguments "{type(args[0]).__name__}" or "{type(args[1]).__name__}"')

        if len(args) == 1:
            if isinstance(args[0], Matrix):
                self.__matrix = args[0].__matrix[:][:]

                return

            if isinstance(args[0], list):
                if all(isinstance(vector, Vector) for vector in args[0]):
                    self.__matrix = []
                    max_size = len(max(args[0], key=len))

                    for i in range(len(args[0])):
                        self.__matrix.append(Vector(max_size, list(args[0][i])))

                    return

                if all(isinstance(vector, list) for vector in args[0]):
                    if all(isinstance(item, int | float) for vector in args[0] for item in vector):
                        self.__matrix = []
                        max_size = len(max(args[0], key=len))

                        for i in range(len(args[0])):
                            self.__matrix.append(Vector(max_size, args[0][i]))

                        return

                    raise TypeError('Incorrect type of values')

                raise TypeError(f'Incorrect type of arguments "{type(args[0]).__name__}"')

        raise ValueError('Invalid number of arguments 0')

    @property
    def size(self):
        return len(self.__matrix[0]), len(self.__matrix)

    def __len__(self):
        return len(self.__matrix)

    def __hash__(self):
        return hash(tuple(tuple(vector) for vector in self.__matrix))

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size != other.size:
            raise ValueError

        for item_1, item_2 in zip(self.__matrix, other.__matrix):
            if item_1 != item_2:
                return False

        return True

    def __repr__(self):
        return '{%s}' % ', '.join(map(str, self.__matrix))

    def __str__(self):
        matrix = ''
        width = len(str(max(item for row in self.__matrix for item in row)))

        for row in self.__matrix:
            for item in row:
                matrix += str(item).center(width) + ' '

            matrix += '\n'

        return matrix

    def __getitem__(self, item):
        return self.__matrix[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Index must be int')

        if key < 0 or key >= self.size[1]:
            raise IndexError(f'Incorrect index value, must be in ({0, self.size[1] - 1})')

        if isinstance(value, list):
            self.__matrix[key] = Vector(value)

            return

        if isinstance(value, Vector):
            self.__matrix[key] = Vector(list(value))

            return

        raise TypeError('Vector component must be a list or class Vector')

    def __imul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError

        for i in range(self.size[1]):
            for j in range(self.size[0]):
                self.__matrix[i][j] *= other

        return self

    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size != other.size:
            raise ValueError

        for i in range(self.size[1]):
            for j in range(self.size[0]):
                self.__matrix[i][j] += other.__matrix[i][j]

        return self

    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size != other.size:
            raise ValueError

        for i in range(self.size[1]):
            for j in range(self.size[0]):
                self.__matrix[i][j] -= other.__matrix[i][j]

        return self

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size != other.size:
            raise ValueError

        row = []

        for i in range(self.size[1]):
            row.append(self.__matrix[i] + other.__matrix[i])

        return Matrix(row)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size != other.size:
            raise ValueError

        row = []

        for i in range(self.size[1]):
            row.append(self.__matrix[i] - other.__matrix[i])

        return Matrix(row)

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            other_size = other.size[1], other.size[0]

            if self.size != other_size:
                raise ValueError

            product = []

            for i in range(self.size[0]):
                row = []

                for j in range(self.size[1]):
                    item = 0

                    for k in range(self.size[0]):
                        item += self.__matrix[i][k] * other.__matrix[k][j]

                    row.append(item)

                product.append(row)

            return Matrix(product)

        if isinstance(other, Vector):
            other_size = len(other)

            if self.size[0] != other_size:
                raise ValueError

            vector = []

            for i in range(self.size[1]):
                item = 0

                for j in range(other_size):
                    item += self[i][j] * other[j]

                vector.append(item)

            return Vector(vector)

        raise TypeError

    def get_column(self, item):
        if isinstance(item, int):
            if 0 <= item < self.size[0]:
                return Vector([column[item] for column in self.__matrix])

            raise ValueError

        raise TypeError

    def transpose(self):
        return Matrix([list(vector) for vector in zip(*self.__matrix)])

    def get_minor(self, i):
        return Matrix([list(vector)[:i] + list(vector)[i + 1:] for vector in self.__matrix[1:]])

    def get_determinant(self):
        size = self.size

        if size[0] != size[1]:
            raise ValueError

        if size[0] == 2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0]

        determinant = 0

        for i in range(size[0]):
            determinant += (-1) ** i * self.__matrix[0][i] * self.get_minor(i).get_determinant()

        return determinant


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix_2 = Matrix(2, 3)
# matrix_3 = Matrix(matrix_1)

matrix_3 = Matrix([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
print(matrix_1)
print(matrix_3)
# print(matrix_2)
# print(matrix_3)
# matrix_1[0] = Vector([4, 3, 2, 1])

# matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_11 = Matrix([[2, 1], [1, 2], [3, 4]])
matrix_2 = Matrix([[2, 2, 3], [4, 5, 6], [7, 8, 10]])
matrix_3 = Matrix([[1, 2], [2, 1]])
vector_1 = Vector([3, 4])

print(len(matrix_2))
