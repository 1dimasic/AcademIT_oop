from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        if not isinstance(side_length, int | float):
            raise TypeError(f'Длина стороны квадрата должна быть числом, а не {type(side_length).__name__}')

        self.__side_length = side_length

    @property
    def get_width(self):
        return self.__side_length

    @property
    def get_height(self):
        return self.__side_length

    def get_perimetr(self):
        return 4 * self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def __hash__(self):
        return hash((self.__side_length,))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__side_length == other.__side_length

        return False

    def __str__(self):
        return '%s, длина стороны = %s' % (self.__class__.__name__, self.__side_length)


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        coordinates = (x1, y1, x2, y2, x3, y3)

        for coordinate in coordinates:
            if not isinstance(coordinate, int | float):
                raise TypeError(f'Координаты должны быть числом, а не {type(coordinate).__name__}')

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    @property
    def get_width(self):
        return max(self.__x1, self.__x2, self.__x3) - min(self.__x1, self.__x2, self.__x3)

    @property
    def get_height(self):
        return max(self.__y1, self.__y2, self.__y3) - min(self.__y1, self.__y2, self.__y3)

    def get_sides_length(self):
        side_a = math.sqrt(pow(self.__x2 - self.__x1, 2) + pow(self.__y2 - self.__y1, 2))
        side_b = math.sqrt(pow(self.__x3 - self.__x2, 2) + pow(self.__y3 - self.__y2, 2))
        side_c = math.sqrt(pow(self.__x1 - self.__x3, 2) + pow(self.__y1 - self.__y3, 2))

        return side_a, side_b, side_c

    def get_perimetr(self):
        perimetr = 0

        for side in self.get_sides_length():
            perimetr += side

        return perimetr

    def get_area(self):
        perimetr_half = self.get_perimetr() / 2
        area = perimetr_half

        for side in self.get_sides_length():
            area *= perimetr_half - side

        return math.sqrt(area)

    def __hash__(self):
        return hash((self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__x1 == other.__x1 and self.__y1 == other.__y1 and \
                   self.__x2 == other.__x2 and self.__y2 == other.__y2 and \
                   self.__x3 == other.__x3 and self.__y3 == other.__y3

        return False

    def __str__(self):
        return '%s, координаты вершин (x1,y1) = (%s,%s), (x2,y2) = (%s,%s), (x3,y3) = (%s,%s)' \
               % (self.__class__.__name__, self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3)


class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, int | float):
            raise TypeError(f'Ширина прямоугольника должна быть числом, а не {type(width).__name__}')

        if not isinstance(height, int | float):
            raise TypeError(f'Высота прямоугольника должна быть числом, а не {type(height).__name__}')

        self.__width = width
        self.__height = height

    @property
    def get_width(self):
        return self.__width

    @property
    def get_height(self):
        return self.__height

    def get_perimetr(self):
        return 2 * self.__height + 2 * self.__width

    def get_area(self):
        return self.__height * self.__width

    def __hash__(self):
        return hash((self.__width, self.__height))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__width == other.__width and self.__height == other.__height

        return False

    def __str__(self):
        return '%s, ширина = %s, высота = %s' % (self.__class__.__name__, self.__width, self.__height)


class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, int | float):
            raise TypeError(f'Радиус окружности должен быть числом, а не {type(radius).__name__}')

        self.__radius = radius

    @property
    def get_width(self):
        return 2 * self.__radius

    @property
    def get_height(self):
        return 2 * self.__radius

    def get_perimetr(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * pow(self.__radius, 2)

    def __hash__(self):
        return hash((self.__radius,))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__radius == other.__radius

        return False

    def __str__(self):
        return '%s, радиус = %s' % (self.__class__.__name__, self.__radius)
