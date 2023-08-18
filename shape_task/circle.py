from shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, int | float):
            raise TypeError(f'Радиус окружности должен быть числом, а не {type(radius).__name__}')

        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def get_width(self):
        return 2 * self.__radius

    def get_height(self):
        return 2 * self.__radius

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def __hash__(self):
        return hash(self.__radius)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__radius == other.__radius

        return False

    def __repr__(self):
        return '%s, радиус = %s' % (self.__class__.__name__, self.__radius)
