from list_task.list_item import ListItem


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def get_first(self):
        if self.__count == 0:
            raise IndexError('List is empty')

        return self.__head.data

    def add_first(self, data):
        self.__head = ListItem(data, self.__head)
        self.__count += 1

    def delete_first(self):
        if self.__count == 0:
            raise IndexError('List is empty')

        deleted_data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1

        return deleted_data

    def reverse(self):
        if self.__count <= 1:
            return

        previous_item = None
        current_item = self.__head

        while current_item:
            next_item = current_item.next
            current_item.next = previous_item
            previous_item = current_item
            current_item = next_item

        self.__head = previous_item

    def copy(self):
        list_copy = SinglyLinkedList()
        list_copy.__count = self.__count

        if list_copy.__count == 0:
            return list_copy

        current_item = self.__head
        list_copy.__head = current_item
        list_copy_current_item = list_copy.__head

        while current_item.next:
            current_item = current_item.next
            list_copy_current_item.next.data = current_item.data
            list_copy_current_item = list_copy_current_item.next

        return list_copy

    def insert(self, index, data):
        self.__check_key(index, self.__count + 1)

        if index == 0:
            self.add_first(data)

            return

        previous_item = self.__get_item(index - 1)
        current_item = previous_item.next
        previous_item.next = ListItem(data, current_item)
        self.__count += 1

    @staticmethod
    def __check_key(key, size):
        if not isinstance(key, int):
            raise TypeError(f'Incorrect type of argument "{type(key).__name__}", must be int')

        if key < 0 or key >= size:
            raise IndexError(f'Incorrect index value, must be in ({0, size - 1}), not {key}')

    def __getitem__(self, key):
        self.__check_key(key, self.__count)

        return self.__get_item(key).data

    def __setitem__(self, key, data):
        self.__check_key(key, self.__count)

        current_item = self.__get_item(key)
        current_item.data = data

    def __delitem__(self, key):
        self.__check_key(key, self.__count)

        if key == 0:
            return self.delete_first()

        previous_item = self.__get_item(key - 1)
        current_item = previous_item.next
        previous_item.next = current_item.next
        self.__count -= 1

        return current_item.data

    def delete_by_value(self, data):
        current_item = self.__head
        previous_item = None

        while current_item:
            if current_item.data == data:
                if previous_item is None:
                    self.__head = self.__head.next
                else:
                    previous_item.next = current_item.next

                self.__count -= 1
                return True

            previous_item = current_item
            current_item = current_item.next

        return False

    def __repr__(self):
        output_list = []

        if self.__count == 0:
            return str(output_list)

        current_item = self.__head

        while current_item:
            output_list.append(current_item.data)
            current_item = current_item.next

        return str(output_list)

    def __get_item(self, index):
        current_item = self.__head
        current_index = 0

        while current_item:
            if current_index == index:
                return current_item

            current_item = current_item.next
            current_index += 1

        raise IndexError(f'Incorrect index value, must be in ({0, self.__count - 1}), not {index}')
