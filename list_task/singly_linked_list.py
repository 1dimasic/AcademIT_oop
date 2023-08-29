from list_task.list_item import ListItem


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def get_size(self):
        return self.__count

    def get_first_item(self):
        return self.__head.data

    def add(self, data):
        new_item = ListItem(data, self.__head)
        self.__head = new_item
        self.__count += 1

    def delete(self):
        value = self.__head.data
        self.__head = self.__head.next_
        self.__count -= 1

        return value

    def reverse(self):
        previous_item = None
        current_item = self.__head
        next_item = current_item.next_

        while current_item:
            current_item.next_ = previous_item
            previous_item = current_item
            current_item = next_item

            if next_item:
                next_item = next_item.next_

        self.__head = previous_item

    def copy(self):
        current_item = self.__head
        current_index = 0
        other = SinglyLinkedList()

        while current_item:
            other.insert(current_index, current_item.data)
            current_index += 1
            current_item = current_item.next_

        return other

    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f'Incorrect type of argument "{type(index).__name__}"')

        if index < 0 or index > self.__count:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__count})')

        if index == 0:
            self.add(data)

            return

        new_item = ListItem(data)
        current_item = self.__head
        previous_item = None
        current_index = 0

        while current_item:
            if current_index == index:
                new_item.next_ = previous_item.next_
                previous_item.next_ = new_item
                self.__count += 1

                return

            previous_item = current_item
            current_item = current_item.next_
            current_index += 1

        previous_item.next_ = new_item
        self.__count += 1

    @staticmethod
    def check_type_key(key):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

    def __getitem__(self, item):
        self.check_type_key(item)

        if item < 0 or item > self.__count - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__count - 1})')

        current_item = self.__head
        current_index = 0

        while current_item:
            if current_index == item:
                return current_item.data

            current_index += 1
            current_item = current_item.next_

        return None

    def __setitem__(self, key, value):
        self.check_type_key(key)

        if key < 0 or key > self.__count - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__count - 1})')

        current_item = self.__head
        current_index = 0

        while current_item:
            if current_index == key:
                current_item.data = value
                return

            current_index += 1
            current_item = current_item.next_

    def __delitem__(self, key):
        self.check_type_key(key)

        if key < 0 or key > self.__count - 1:
            raise IndexError(f'Incorrect index value, must be in ({0, self.__count - 1})')

        if key == 0:
            self.delete()
            return

        current_item = self.__head
        previous_item = None
        current_index = 0

        while current_item:
            if current_index == key:
                previous_item.next_ = current_item.next_
                current_item.next_ = None
                self.__count -= 1

                return current_item.data

            previous_item = current_item
            current_item = current_item.next_
            current_index += 1

    def delete_by_value(self, value):
        current_item = self.__head
        previous_item = None

        while current_item:
            if current_item.data == value:
                previous_item.next_ = current_item.next_
                current_item.next_ = None
                self.__count -= 1

                return True

            previous_item = current_item
            current_item = current_item.next_

        return False

    def __repr__(self):
        current_item = self.__head
        singly_linked_list = ''

        while current_item:
            singly_linked_list += str(current_item.data) + ' '
            current_item = current_item.next_

        return singly_linked_list
