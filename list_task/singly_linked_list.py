from list_task.list_item import ListItem


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def get_first(self):
        if not self.__count:
            raise ValueError('List is empty')

        return self.__head.data

    def add(self, data):
        self.__head = ListItem(data, self.__head)
        self.__count += 1

    def delete_first(self):
        try:
            data = self.__head.data
        except AttributeError:
            raise AttributeError('List is empty')

        self.__head = self.__head.next
        self.__count -= 1

        return data

    def reverse(self):
        previous_item = None
        current_item = self.__head

        try:
            next_item = current_item.next
        except AttributeError:
            raise AttributeError('List is empty')

        while current_item:
            current_item.next = previous_item
            previous_item = current_item
            current_item = next_item

            if next_item:
                next_item = next_item.next

        self.__head = previous_item

    def copy(self):
        current_item = self.__head
        other = SinglyLinkedList()

        while current_item:
            other.add(current_item.data)
            current_item = current_item.next

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
        previous_item, current_item = self.__get_two_neighboring_item_by_index(index)

        previous_item.next = new_item
        new_item.next = current_item
        self.__count += 1

    @staticmethod
    def __check_key(key, size):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}"')

        if key < 0 or key >= size:
            raise IndexError(f'Incorrect index value, must be in ({0, size - 1}), not {key}')

    def __get_two_neighboring_item_by_index(self, index):
        current_item = self.__head
        previous_item = None
        current_index = 0

        while current_item:
            if current_index != index:
                previous_item = current_item
                current_item = current_item.next
                current_index += 1
                continue

            break

        return previous_item, current_item

    def __getitem__(self, item):
        self.__check_key(item, self.__count)

        current_item = self.__head
        current_index = 0

        while current_item:
            if current_index == item:
                return current_item.data

            current_index += 1
            current_item = current_item.next

        return None

    def __setitem__(self, key, data):
        self.__check_key(key, self.__count)

        current_item = self.__head
        current_index = 0

        while current_item:
            if current_index == key:
                current_item.data = data
                return

            current_index += 1
            current_item = current_item.next

    def __delitem__(self, key):
        self.__check_key(key, self.__count)

        if key == 0:
            self.delete()
            return

        previous_item, current_item = self.__get_two_neighboring_item_by_index(key)

        previous_item.next = current_item.next
        current_item.next = None
        self.__count -= 1

        return current_item.data

    def delete_by_value(self, data):
        current_item = self.__head
        previous_item = None

        while current_item:
            if current_item.data == data:
                if previous_item is None:
                    self.__head = current_item.next
                    current_item.next = None
                    self.__count -= 1

                    return True

                previous_item.next = current_item.next
                current_item.next = None
                self.__count -= 1

                return True

            previous_item = current_item
            current_item = current_item.next

        return False

    def __repr__(self):
        current_item = self.__head
        list_string = ''

        while current_item and current_item.next:
            list_string += str(current_item.data) + ', '
            current_item = current_item.next

        list_string = '[' + list_string + str(current_item.data) + ']'

        return list_string
