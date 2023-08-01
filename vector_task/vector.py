class Vector:
    def __init__(self, size=None, components=None):
        if isinstance(size, int):
            if size <= 0:
                raise ValueError('Размерность вектора должна быть больше нуля.')
            else:
                if components is None:
                    components = size * [0]
                else:
                    oversize = size - len(components)

                    if oversize > 0:
                        components.extend(oversize * [0])

                self.__components = components

        if isinstance(size, Vector):
            self.__components = size.__components

        if isinstance(size, list):
            self.__components = size

    def __repr__(self):
        return f'{self.__components}'


vector_1 = Vector(2)
vector_2 = Vector(3, [1, 2, 4])
vector_3 = Vector(vector_2)
vector_4 = Vector([1, 5, 4])
vector_5 = Vector(5, [3, 2, 1])

print(vector_1, vector_2, vector_3, vector_4, vector_5)
