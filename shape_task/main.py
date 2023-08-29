from triangle import Triangle
from square import Square
from rectangle import Rectangle
from circle import Circle


def get_max_area_shape(shapes):
    if not shapes:
        raise IndexError('Список фигур пуст')

    return sorted(shapes, key=lambda shape: shape.get_area(), reverse=True)[0]


def get_second_largest_perimeter_shape(shapes):
    if len(shapes) <= 1:
        raise ValueError('Список состоит из одной фигуры или пуст')

    return sorted(shapes, key=lambda shape: shape.get_perimeter(), reverse=True)[1]


# площадь; периметр
triangle_1 = Triangle(1, 1, 4, 1, 1, 5)  # 6; 12
triangle_2 = Triangle(-5, 0, 0, 5, 5, 0)  # 25; 24,14
square_1 = Square(2)  # 4; 8
square_2 = Square(4)  # 16; 16
rectangle_1 = Rectangle(2, 4)  # 8; 12
rectangle_2 = Rectangle(2, 5)  # 10; 14
circle_1 = Circle(5)  # 78.5; 31,4
circle_2 = Circle(3)  # 28.26; 18,84

shapes_list = [triangle_1, triangle_2, square_1, square_2, rectangle_1, rectangle_2, circle_1, circle_2]
print(f'Максимальная площадь у фигуры {get_max_area_shape(shapes_list)}')
print(f'Второй по величине периметр у фигуры {get_second_largest_perimeter_shape(shapes_list)}')
