class Field:
    def __init__(self):
        self.__data = 0
        self.__is_flag = False

    # TODO validation
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def is_flag(self):
        return self.__is_flag

    @is_flag.setter
    def is_flag(self, is_flag):
        self.__is_flag = is_flag
