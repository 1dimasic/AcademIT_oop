from matrix_task.matrix import Matrix
from vector_task.vector import Vector

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# проверка __getitem__, __setitem__
print(f'Первая строка матрицы {matrix_1[0]}')
matrix_1[1] = Vector(3, [-1, -1])
print(f'Матрица после изменения второй строки {matrix_1}')

# проверка __mul__, __rmul__, _imul__
matrix_result = 2 * matrix_1 * 2
print(f'Результат умножения на скаляр с обеих сторон {matrix_result}')
matrix_result *= 3
print(f'Результат умножения на скаляр на месте {matrix_result}')

# проверка __iadd__, __isub__
matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, 9]])
matrix_1 += matrix_3
print(f'Результат прибавления к матрице матрицы равен {matrix_1}')
matrix_1 -= matrix_3
print(f'Результат вычитания от матрицы матрицы равен {matrix_1}')

# проверка __add__, __sub__, __matmul__
matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
matrix_result = matrix_1 + matrix_2
print(f'Результат сложения двух матриц равен {matrix_result}')
matrix_result = matrix_1 - matrix_2
print(f'Результат вычитания двух матриц равен {matrix_result}')
matrix_result = matrix_1 @ matrix_2
print(f'Результат умножения двух матриц равен {matrix_result}')
vector_1 = Vector([3, 4, 5])
vector_result = matrix_1 @ vector_1
print(f'Результат умножения матрицы на вектор столбец равен {vector_result}')

# проверка __eq__
matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix(matrix_1)
matrix_3 = Matrix([[1, 2], [3, 40]])
print(f'Матрица {matrix_1} равна матрице {matrix_2}.....{matrix_1 == matrix_2}')
print(f'Матрица {matrix_1} равна матрице {matrix_3}.....{matrix_1 == matrix_3}')

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Вектор-столбец под индексом 0 равен {matrix_1.get_column(0)}')
matrix_1.transpose()
print(f'Транспонированная матрица {matrix_1}')
print(f'Определитель матрицы равен {matrix_1.get_determinant()}')
