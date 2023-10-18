from lambda_task.person import Person

people = [Person('Витя', 25),
          Person('Иван', 50),
          Person('Олег', 45),
          Person('Игорь', 17),
          Person('Вася', 29),
          Person('Вася', 10)]

# получить людей, возраст которых от 20 до 45, вывести в консоль их имена в порядке убывания возраста
list_of_people_aged_20_to_45 = sorted(filter(lambda x: 20 <= x.age <= 45, people), key=lambda x: x.age, reverse=True)
print('Имена людей, возраст от 20 до 45, в порядке убывания:', end=' ')
for person in list_of_people_aged_20_to_45:
    print(person.name, end=' ')

print()

# получить список людей младше 18, посчитать для них средний возраст
names_of_people_under_18 = list(map(lambda name: name.name, filter(lambda x: x.age < 18, people)))
ages_of_people_under_18 = list(map(lambda age: age.age, filter(lambda x: x.age < 18, people)))

if ages_of_people_under_18:
    average_age = sum(ages_of_people_under_18)/len(ages_of_people_under_18)
    print(f'Список людей младше 18: {names_of_people_under_18}, их средний возраст = {average_age}')

# получить список уникальных имен
unique_names = list(set(map(lambda x: x.name, people)))
print('Имена:', end=' ')
for i in range(len(unique_names)):
    print(unique_names[i], end=', ' if i < len(unique_names) - 1 else '.')
