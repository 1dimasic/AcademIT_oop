import math
from shape import Shape


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        coordinates = x1, y1, x2, y2, x3, y3

        for i in range(len(coordinates)):
            if not isinstance(coordinates[i], int | float):
                coordinate_name = 'x' if i % 2 == 0 else 'y'
                coordinate_index = i // 2 + 1

                raise TypeError(f'Координаты должны быть числом. Сейчас {coordinate_name}{coordinate_index} '
                                f'{type(coordinates[i]).__name__}')

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    @property
    def x1(self):
        return self.__x1

    @x1.setter
    def x1(self, x1):
        self.__x1 = x1

    @property
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, y1):
        self.__y1 = y1

    @property
    def x2(self):
        return self.__x2

    @x2.setter
    def x2(self, x2):
        self.__x2 = x2

    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, y2):
        self.__y2 = y2

    @property
    def x3(self):
        return self.__x3

    @x3.setter
    def x3(self, x3):
        self.__x3 = x3

    @property
    def y3(self):
        return self.__y3

    @y3.setter
    def y3(self, y3):
        self.__y3 = y3

    def get_width(self):
        return max(self.__x1, self.__x2, self.__x3) - min(self.__x1, self.__x2, self.__x3)

    def get_height(self):
        return max(self.__y1, self.__y2, self.__y3) - min(self.__y1, self.__y2, self.__y3)

    @staticmethod
    def __get_side_length(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    def get_sides_lengths(self):
        side_1_length = self.__get_side_length(self.__x1, self.__y1, self.__x2, self.__y2)
        side_2_length = self.__get_side_length(self.__x2, self.__y2, self.__x3, self.__y3)
        side_3_length = self.__get_side_length(self.__x3, self.__y3, self.__x1, self.__y1)

        return side_1_length, side_2_length, side_3_length

    def get_perimeter(self):
        return sum(self.get_sides_lengths())

    def get_area(self):
        sides_lengths = self.get_sides_lengths()
        perimeter_half = sum(sides_lengths) / 2
        area = perimeter_half

        for side_length in sides_lengths:
            area *= perimeter_half - side_length

        return math.sqrt(area)

    def __hash__(self):
        return hash((self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__x1 == other.__x1 and self.__y1 == other.__y1 and \
                   self.__x2 == other.__x2 and self.__y2 == other.__y2 and \
                   self.__x3 == other.__x3 and self.__y3 == other.__y3

        return False

    def __repr__(self):
        return '%s, координаты вершин: (%s, %s), (%s, %s), (%s, %s)' \
               % (self.__class__.__name__, self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3)
