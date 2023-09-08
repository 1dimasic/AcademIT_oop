from vector import Vector


def print_vector(vector):
    print(f'Вектор {vector}, размерностью = {vector.size}, длиной = {vector.length:.2f}')


vector_1 = Vector(2)
vector_2 = Vector(3, [3, 4, 8])
vector_3 = Vector(vector_2)
vector_4 = Vector([6, -5])
vector_5 = Vector(5, [3, 4, 5])

# проверка методов __init__, __repr__, свойств
print_vector(vector_1)
print_vector(vector_2)
print_vector(vector_3)
print_vector(vector_4)
print_vector(vector_5)
print()

# проверка копирования
vector_2 = Vector(2, [2, 5])
print_vector(vector_2)
print_vector(vector_3)
print()

# проверка методов __iadd__, __isub__, __imul__
vector_5 += vector_2
print(f'Результат операции += равен {vector_5}')
vector_5 -= vector_2
print(f'Результат операции -= равен {vector_5}')
vector_5 *= 5
print(f'Результат операции *= 5 равен {vector_5}')
print()

# проверка методов __add__, __sub__, __mul__
vector_result = vector_3 + vector_4
print(f'Результат операции {vector_3} + {vector_4} равен {vector_result}')
vector_result = vector_3 - vector_4
print(f'Результат операции {vector_3} - {vector_4} равен {vector_result}')
vector_result = vector_3 * 3
print(f'Результат операции {vector_3} * 3 равен {vector_result}')
vector_result = -1 * vector_3
print(f'Результат операции -1 * {vector_3} равен {vector_result}')
print()

# проверка методов __getitem__, __setitem__, __eq__
print(f'Вторая компонента вектора {vector_3} = {vector_3[1]}')
vector_3[0] = 55
print(f'Первая компонента вектора {vector_3} = {vector_3[0]}')

print(f'Результат операции {vector_2} == {vector_3} равен {vector_2 == vector_3}')
vector_2 = Vector(3, [1, 2, 3])
vector_3 = Vector(vector_2)
print(f'Результат операции {vector_2} == {vector_3} равен {vector_2 == vector_3}')

print(f'Результат скалярного произведения векторов {vector_2} * {vector_4} равен {vector_2.get_scalar_product(vector_4)}')
