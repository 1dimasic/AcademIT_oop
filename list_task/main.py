from list_task.singly_linked_list import SinglyLinkedList


def print_list(sl_list):
    print(f'Singly linked list: {sl_list}, size: {len(sl_list)}')


singly_linked_list = SinglyLinkedList()
singly_linked_list.add(2)
singly_linked_list.add(4)
singly_linked_list.add(0)
singly_linked_list.add(5)
singly_linked_list.add(-1)
print_list(singly_linked_list)

singly_linked_list.delete_first()
print_list(singly_linked_list)

singly_linked_list.reverse()
print(f'Reversed singly linked list: {singly_linked_list}')

singly_linked_list_copy = singly_linked_list.copy()
print_list(singly_linked_list_copy)

singly_linked_list.insert(0, -10)
print_list(singly_linked_list)
singly_linked_list.insert(5, -10)
print_list(singly_linked_list)
singly_linked_list.insert(3, 100)
print_list(singly_linked_list)

print(f'singly_linked_list[6] = {singly_linked_list[6]}')
singly_linked_list[6] = -50
print_list(singly_linked_list)
singly_linked_list.__delitem__(1)
print_list(singly_linked_list)

singly_linked_list.delete_by_value(-10)
print_list(singly_linked_list)
