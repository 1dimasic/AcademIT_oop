from shape import Shape


class Square(Shape):
    def __init__(self, side_length):
        if not isinstance(side_length, int | float):
            raise TypeError(f'Длина стороны квадрата должна быть числом, а не {type(side_length).__name__}')

        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length):
        self.__side_length = side_length

    def get_width(self):
        return self.__side_length

    def get_height(self):
        return self.__side_length

    def get_perimeter(self):
        return 4 * self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def __hash__(self):
        return hash(self.__side_length)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__side_length == other.__side_length

        return False

    def __repr__(self):
        return '%s, длина стороны = %s' % (self.__class__.__name__, self.__side_length)
