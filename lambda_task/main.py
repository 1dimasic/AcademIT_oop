from itertools import groupby
from lambda_task.person import Person

persons = [Person('Витя', 25),
           Person('Иван', 50),
           Person('Олег', 45),
           Person('Игорь', 17),
           Person('Вася', 29),
           Person('Вася', 10)]

# получить людей, возраст которых от 20 до 45, вывести в консоль их имена в порядке убывания возраста
persons_aged_20_to_45_list = sorted(filter(lambda x: 20 <= x.age <= 45, persons), key=lambda x: x.age, reverse=True)

print('Имена людей, возраст от 20 до 45, в порядке убывания:', end=' ')

for person in persons_aged_20_to_45_list:
    print(person.name, end=', ')

print()

# получить список людей младше 18, посчитать для них средний возраст
persons_aged_to_18_list = list(filter(lambda p: p.age < 18, persons))
persons_aged_to_18_ages_list = list(map(lambda p: p.age, persons_aged_to_18_list))
persons_aged_to_18_names_list = list(map(lambda p: p.name, persons_aged_to_18_list))

if len(persons_aged_to_18_ages_list) != 0:
    average_age = sum(persons_aged_to_18_ages_list) / len(persons_aged_to_18_ages_list)
    print(f'Список людей младше 18: {", ".join(map(str, persons_aged_to_18_names_list))}, '
          f'их средний возраст = {average_age}.')
else:
    print('Нет людей младше 18 лет')

# получить список уникальных имен
unique_names = list(set(map(lambda x: x.name, persons)))

print('Имена:', end=' ')

for i in range(len(unique_names)):
    print(unique_names[i], end=', ' if i < len(unique_names) - 1 else '.')

print()

# получить словарь, в котором ключи – имена, а значения – средний возраст
name_average_age_dict = {group[0].name: sum(list(map(lambda p: p.age, group))) / len(group) for group in
                         [list(group) for name, group in groupby(persons, key=lambda p: p.name)]}

print(f'Словарь "имя":средний возраст: {name_average_age_dict}')
