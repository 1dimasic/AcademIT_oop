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
        if not isinstance(other, TreeNode | None):
            raise TypeError(f'Type of argument must be TreeNode class, not {type(other).__name__}')

        self.__left = other

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, other):
        if not isinstance(other, TreeNode | None):
            raise TypeError(f'Type of argument must be TreeNode class, not {type(other).__name__}')

        self.__right = other

    @property
    def data(self):
        return self.__data
