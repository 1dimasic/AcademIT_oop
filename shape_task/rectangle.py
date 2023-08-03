from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, int | float):
            raise TypeError(f'Ширина прямоугольника должна быть числом, а не {type(width).__name__}')

        if not isinstance(height, int | float):
            raise TypeError(f'Высота прямоугольника должна быть числом, а не {type(height).__name__}')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_perimeter(self):
        return 2 * (self.__height + self.__width)

    def get_area(self):
        return self.__height * self.__width

    def __hash__(self):
        return hash((self.__width, self.__height))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__width == other.__width and self.__height == other.__height

        return False

    def __repr__(self):
        return '%s, ширина = %s, высота = %s' % (self.__class__.__name__, self.__width, self.__height)
