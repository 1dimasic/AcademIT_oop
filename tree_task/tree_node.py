class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, other):
        self.__left = other

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, other):
        self.__right = other

    @property
    def data(self):
        return self.__data

    def __repr__(self):
        return str(self.__data)