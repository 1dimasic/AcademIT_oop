from range import Range

# тестовая программа для проверки класса Range
start_point = float(input('Введите начало интервала: '))
end_point = float(input('Введите конец интервала: '))
point_a = float(input('Введите координату точки А: '))

current_range = Range(start_point, end_point)

if current_range.is_inside(point_a):
    print(f'Точка A находится внутри интервала {current_range}')
    range_1 = Range(start_point, point_a)
    range_2 = Range(point_a, end_point)
    print(
        f'Расстояние от начала интервала до точки A = {range_1.length:.2f}, '
        f'расстояние от точки A до конца интервала = {range_2.length:.2f}')
else:
    print(f'Точка А не находится внутри интервала {current_range}')

# тестовая программа для проверки методов класса Range*
start_1 = float(input('Введите начало первого интервала: '))
end_1 = float(input('Введите конец первого интервала: '))
start_2 = float(input('Введите начало второго интервала: '))
end_2 = float(input('Введите конец второго интервала: '))

range_1 = Range(start_1, end_1)
range_2 = Range(start_2, end_2)

print(f'Пересечение интервалов {range_1} и {range_2} = {range_1.get_intersection(range_2)}')
print(f'Объединение интервалов {range_1} и {range_2} = {range_1.get_union(range_2)}')
print(f'Разность интервалов {range_1} и {range_2} = {range_1.get_difference(range_2)}')
