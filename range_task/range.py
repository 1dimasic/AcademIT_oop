class Range:
    def __init__(self, start, end):
        if start > end:
            start, end = end, start

        self.__start = start
        self.__end = end
        self.__length = end - start

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

    @property
    def length(self):
        return self.__length

    def is_inside(self, point):
        return self.__start <= point <= self.__end

    def get_intersection(self, range_2):
        if max(self.__start, range_2.__start) < min(self.__end, range_2.__end):
            return Range(max(self.__start, range_2.__start), min(self.__end, range_2.__end))

        return None

    def get_union(self, range_2):
        if max(self.__start, range_2.__start) <= min(self.__end, range_2.__end):
            return Range(min(self.__start, range_2.__start), max(self.__end, range_2.__end))

        return [Range(self.__start, self.__end), Range(range_2.__start, range_2.__end)]

    def get_difference(self, range_2):
        if self.__start > range_2.__start and self.__end < range_2.__end:
            return []

        if self.__start < range_2.__start and self.__end > range_2.__end:
            return Range(self.__start, range_2.__start)

        if self.__start < range_2.__start < self.__end:
            return Range(self.__start, range_2.__start)

        if self.__start < range_2.__end < self.__end:
            return Range(range_2.__end, self.__end)

        return [Range(self.__start, self.__end), Range(range_2.__start, range_2.__end)]

    def __repr__(self):
        return '(%s; %s)' % (self.__start, self.__end)
