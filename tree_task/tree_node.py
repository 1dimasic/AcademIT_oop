class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @left.setter
    def left(self, other):
        self.__left = other

    @right.setter
    def right(self, other):
        self.__right = other

    @property
    def data(self):
        return self.__data

    def __repr__(self):
        return '%s' % self.__data
