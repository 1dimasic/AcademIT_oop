class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def get_size(self):
        return self.__count

    def get_first_item(self):
        return self.__head.data

    def add(self, data):
        list_item = ListItem(data, self.__head)
        self.__head = list_item
        self.__count += 1

    def delete(self):
        value = self.__head.data
        self.__head = self.__head.next_item
        self.__count -= 1

        return value

    def reverse(self):
        previous_item = None
        current_item = self.__head
        next_item = current_item.next_item

        while current_item:
            current_item.next_item = previous_item
            previous_item = current_item
            current_item = next_item

            if next_item:
                next_item = next_item.next_item

        self.__head = previous_item

    def copy(self):
        current_item = self.__head
        current_index = 0
        other = SinglyLinkedList()

        while current_item:
            other.insert(current_index, current_item.data)
            current_item = current_item.next_item
            current_index += 1

        return other

    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError

        if index < 0 or index > self.__count:
            raise IndexError

        if index == 0:
            self.add(data)

            return

        new_item = ListItem(data)
        current_item = self.__head
        previous_item = None
        current_index = 0

        while current_item is not None:
            if current_index == index:
                new_item.next_item = previous_item.next_item
                previous_item.next_item = new_item

                return

            previous_item = current_item
            current_item = current_item.next_item
            current_index += 1

        self.__count += 1

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError

        if item < 0 or item > self.__count:
            raise IndexError

        current_item = self.__head
        current_index = 0

        while current_item is not None:
            if current_index == item:
                return current_item.data

            current_index += 1
            current_item = current_item.next_item

        return None

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError

        if key < 0 or key > self.__count:
            raise IndexError

        current_item = self.__head
        current_index = 0

        while current_item is not None:
            if current_index == key:
                current_item.data = value
                return

            current_index += 1
            current_item = current_item.next_item

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        if key < 0 or key > self.__count:
            raise IndexError

        current_item = self.__head
        previous_item = None
        current_index = 0

        while current_item is not None:
            if current_index == key:
                previous_item.next_item = current_item.next_item
                current_item.next_item = None

                return current_item.data

            previous_item = current_item
            current_item = current_item.next_item
            current_index += 1

        self.__count -= 1

    def delete_by_value(self, value):
        current_item = self.__head
        previous_item = None

        while current_item is not None:
            if current_item.data == value:
                previous_item.next_item = current_item.next_item
                current_item.next_item = None

                return True

            previous_item = current_item
            current_item = current_item.next_item

        return False

    def __repr__(self):
        current_item = self.__head
        lst = ''

        while current_item is not None:
            lst += str(current_item.data) + ' '
            current_item = current_item.next_item

        return lst


class ListItem:
    def __init__(self, data, next_item=None):
        self.__data = data
        self.__next_item = next_item

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_item(self):
        return self.__next_item

    @next_item.setter
    def next_item(self, next_item):
        self.__next_item = next_item


lst = SinglyLinkedList()
lst.add(4)
lst.add(3)
lst.add(2)
lst.add(1)
print(lst)
lst_1 = lst.copy()
print(lst_1)
