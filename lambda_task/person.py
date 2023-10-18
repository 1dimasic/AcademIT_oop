class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError(f'Incorrect type {type(name).__name__}, must be str')

        if not isinstance(age, int):
            raise TypeError(f'Incorrect type {type(age).__name__}, must be int')

        if age <= 0:
            raise ValueError(f'Age must be > 0, not {age}')

        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'Incorrect type {type(name).__name__}, must be str')

        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError(f'Incorrect type {type(age).__name__}, must be int')

        if age <= 0:
            raise ValueError(f'Age must be > 0, not {age}')

        self.__age = age
