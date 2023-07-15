from range import Range

start_1 = float(input('Введите начало первого интервала: '))
end_1 = float(input('Введите конец первого интервала: '))
start_2 = float(input('Введите начало второго интервала: '))
end_2 = float(input('Введите конец второго интервала: '))

range_1 = Range(start_1, end_1)
range_2 = Range(start_2, end_2)

print(f'Пересечение интервалов {range_1} и {range_2} = {range_1.get_intersection(range_2)}')
print(f'Объединение интервалов {range_1} и {range_2} = {range_1.get_union(range_2)}')
print(f'Разность интервалов {range_1} и {range_2} = {range_1.get_difference(range_2)}')
