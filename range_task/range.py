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

    @property
    def length(self):
        return self.__end - self.__start

    def is_inside(self, point):
        return self.__start <= point <= self.__end

    def get_intersection(self, other_range):
        max_start = max(self.__start, other_range.__start)
        min_end = min(self.__end, other_range.__end)

        if max_start < min_end:
            return Range(max_start, min_end)

        return None

    def get_union(self, other_range):
        if max(self.__start, other_range.__start) <= min(self.__end, other_range.__end):
            return Range(min(self.__start, other_range.__start), max(self.__end, other_range.__end))

        return [Range(self.__start, self.__end), Range(other_range.__start, other_range.__end)]

    def get_difference(self, other_range):
        if self.__start >= other_range.__start and self.__end <= other_range.__end:
            return []

        if self.__start < other_range.__start and self.__end > other_range.__end:
            return [Range(self.__start, other_range.__start), Range(other_range.__start, self.__end)]

        if self.__start < other_range.__start < self.__end:
            return Range(self.__start, other_range.__start)

        if self.__start < other_range.__end < self.__end:
            return Range(other_range.__end, self.__end)

        return Range(self.__start, self.__end)

    def __repr__(self):
        return f'({self.__start}, {self.__end})'
