from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError

        if len(args) == 2:
            if all(isinstance(arg, int) and arg > 0 for arg in args):
                self.__matrix = [Vector(args[0])] * args[1]

                return

            raise TypeError

        if len(args) == 1:
            if isinstance(args[0], Matrix):
                self.__matrix = args[0].__matrix[:][:]

                return

            if isinstance(args[0], list):
                if all(isinstance(vector, Vector) for vector in args[0]):
                    max_size_vector = max(args[0], key=len)
                    a = max_size_vector[:]


                    return

                if all(isinstance(vector, list) for vector in args[0]):
                    if all(isinstance(item, int | float) for vector in args[0] for item in vector):
                        self.__matrix = []
                        max_size = len(max(args[0], key=len))

                        for i in range(len(args[0])):
                            self.__matrix.append(Vector(max_size, args[0][i]))

                        return

                    raise ValueError

                raise ValueError

        if len(args) == 0:
            raise ValueError

    @property
    def size(self):
        return len(self.__matrix[0]), len(self.__matrix)

    def __len__(self):
        return len(self.__matrix)

    def __repr__(self):
        matrix = ''
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                matrix += str(self.__matrix[i][j]) + ' '
            matrix += '\n'

        return matrix

    def __getitem__(self, item):
        return self.__matrix[item]


matrix_1 = Matrix([[1, 2, 3, 4], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix(2, 3)
matrix_3 = Matrix(matrix_1)
print(matrix_3)
matrix_3 = Matrix([Vector([1, 2]), Vector([4, 5, 6]), Vector([7, 8, 9])])
print(matrix_1)
print(matrix_2)
print(matrix_3)
