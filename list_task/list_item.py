class ListItem:
    def __init__(self, data, next_=None):
        self.__data = data
        self.__next_ = next_

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_(self):
        return self.__next_

    @next_.setter
    def next_(self, next_):
        self.__next_ = next_
