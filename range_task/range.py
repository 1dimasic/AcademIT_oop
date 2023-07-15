class Range:
    def __init__(self, start, end):
        if start > end:
            start, end = end, start

        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, point):
        return self.__start <= point <= self.__end

    def get_intersection(self, verifiable_range):
        if self.is_inside(verifiable_range.__start):
            return Range(verifiable_range.__start, min(self.__end, verifiable_range.__end))

        if verifiable_range.is_inside(self.__start):
            return Range(self.__start, min(self.__end, verifiable_range.__end))

    def get_union(self, verifiable_range):
        if self.is_inside(verifiable_range.__start):
            return Range(self.__start, max(self.__end, verifiable_range.__end))

        if verifiable_range.is_inside(self.__start):
            return Range(verifiable_range.__start, max(self.__end, verifiable_range.__end))

        return [self, verifiable_range]

    def get_difference(self, verifiable_range):
        if verifiable_range.is_inside(self.__start) and verifiable_range.is_inside(self.__end):
            return Range(0, 0)

        if self.is_inside(verifiable_range.__start) and self.is_inside(verifiable_range.__end):
            return [Range(self.__start, verifiable_range.__start), Range(verifiable_range.__end, self.__end)]

        if self.is_inside(verifiable_range.__start):
            return Range(self.__start, verifiable_range.__start)

        if self.is_inside(verifiable_range.__end):
            return Range(verifiable_range.__end, self.__end)

        return [self, verifiable_range]

    def __repr__(self):
        return '[%s;%s]' % (self.__start, self.__end)


if __name__ == '__main__':
    start_point = float(input('Введите начало интервала: '))
    end_point = float(input('Введите конец интервала: '))
    point_a = float(input('Введите координату точки А: '))

    current_range = Range(start_point, end_point)

    if current_range.is_inside(point_a):
        print(f'Точка A находится внутри интервала {current_range}')
        range_1 = Range(start_point, point_a)
        range_2 = Range(point_a, end_point)
        print(
            f'Расстояние от начала интервала до точки A = {range_1.get_length():.2f}, '
            f'расстояние от точки A до конца интервала = {range_2.get_length():.2f}')
    else:
        print(f'Точка А не находится внутри интервала {current_range}')
