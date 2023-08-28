class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def get_size(self):
        return self.__count

    def insert_at_beginning(self, data):
        list_item = ListItem(data, self.__head)
        self.__head = list_item
        self.__count += 1

    def delete_at_beginning(self):
        value = self.__head.data
        self.__head = self.__head.next_item
        self.__count -= 1

        return value

    def pivot(self, tail=None):
        current_item = self.__head

        while current_item is not None:
            self.__head, tail, self.__head = tail, self.__head, self.__head.next_item

        return tail

    def insert_by_index(self, index, data):
        if index == 0:
            self.add_at_beginning(data)

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

    def get_by_index(self, index):
        current_item = self.__head
        current_index = 0

        while current_item is not None:
            if current_index == index:
                return current_item.data

            current_index += 1
            current_item = current_item.next_item

        return None

    def delete_item(self, value):
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

    def get_first_item(self):
        return self.__head.data

    def __setitem__(self, key, value):
        if key < 0 or self.__count < key:
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
lst.insert_at_beginning(5)
lst.insert_at_beginning(-2)
lst.insert_at_beginning(6)
lst.insert_at_beginning(0)
lst.insert_at_beginning(9)
print(lst)
lst.pivot()
print(lst)
