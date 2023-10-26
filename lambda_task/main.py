from itertools import groupby

from lambda_task.person import Person

people = [Person('Витя', 25),
          Person('Иван', 50),
          Person('Олег', 45),
          Person('Игорь', 17),
          Person('Вася', 29),
          Person('Вася', 10)]

# # получить людей, возраст которых от 20 до 45, вывести в консоль их имена в порядке убывания возраста
# persons_aged_20_to_45_list = sorted(filter(lambda x: 20 <= x.age <= 45, people), key=lambda x: x.age, reverse=True)
#
# print('Имена людей, возраст от 20 до 45, в порядке убывания:', end=' ')
#
# for person in persons_aged_20_to_45_list:
#     print(person.name, end=', ')
#
# print()
#
# # получить список людей младше 18, посчитать для них средний возраст
# persons_aged_to_18_list = list(filter(lambda p: p.age < 18, people))
# persons_aged_to_18_ages_list = list(map(lambda p: p.age, persons_aged_to_18_list))
# persons_aged_to_18_names_list = list(map(lambda p: p.name, persons_aged_to_18_list))
#
# if len(persons_aged_to_18_ages_list) != 0:
#     average_age = sum(persons_aged_to_18_ages_list)/len(persons_aged_to_18_ages_list)
#     print(f'Список людей младше 18: {", ".join(map(str, persons_aged_to_18_names_list))}, '
#           f'их средний возраст = {average_age}.')
# else:
#     print('Нет людей младше 18 лет')
#
# # получить список уникальных имен
# unique_names = list(set(map(lambda x: x.name, people)))
#
# print('Имена:', end=' ')
#
# for i in range(len(unique_names)):
#     print(unique_names[i], end=', ' if i < len(unique_names) - 1 else '.')

a = [list(grouper) for person, grouper in groupby(people, key=lambda p: p.name)]
print(a)