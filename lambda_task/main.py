from lambda_task.person import Person

person_1 = Person('Витя', 25)
person_2 = Person('Иван', 50)
person_3 = Person('Олег', 21)
person_4 = Person('Игорь', 17)
person_5 = Person('Вася', 29)
person_6 = Person('Вася', 10)

people = [person_1, person_2, person_3, person_4, person_5, person_6]

# получить людей, возраст которых от 20 до 45, вывести в консоль их имена в порядке убывания возраста
names = sorted(list((filter(lambda person: 20 <= person.age <= 45, people))), key=lambda person: person.age,
               reverse=True)
print('Имена людей, возраст от 20 до 45, в порядке убывания:', end=' ')
for name in names:
    print(name.name, end=' ')

print()

# получить список людей младше 18, посчитать для них средний возраст
people_list = list((filter(lambda person: person.age < 18, people)))
people_name_list = list(map(lambda x: x.name, people_list))
average_age = sum(list(map(lambda age: age.age, people_list))) / len(people_list)
print(f'Список людей младше 18: {people_name_list}, их средний возраст = {average_age}')

# получить список уникальных имен
unique_names = set(map(lambda x: x.name, people))
print('Имена:', end=' ')
for i in range(len(unique_names)):
    print(list(unique_names)[i], end=', ' if i < len(unique_names) - 1 else '.')
