class SinglyLinkedList:
    def __init__(self, head, count):
        self.__head = head
        self.__count = count

    @property
    def count(self):
        return self.__count

    @property
    def head(self):
        return self.__head


class ListItem:
    def __init__(self, data, _next=None):
        self.__data = data
        self.__next = _next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def __repr__(self):
        return '%s; %s' % (self.__data, self.__next)


_list = SinglyLinkedList(2, 5)



