from list_task.singly_linked_list import SinglyLinkedList

singly_linked_list = SinglyLinkedList()
singly_linked_list.add_first(2)
singly_linked_list.add_first(4)
singly_linked_list.add_first(0)
singly_linked_list.add_first(5)
singly_linked_list.add_first(-1)
print(f'List: {singly_linked_list}, size: {len(singly_linked_list)}')

singly_linked_list.delete_first()
print(f'List after deleting first item: {singly_linked_list}, size: {len(singly_linked_list)}')

singly_linked_list.reverse()
print(f'List after reverse: {singly_linked_list}, size: {len(singly_linked_list)}')

singly_linked_list_copy = singly_linked_list.copy()
print(f'List copy: {singly_linked_list}, size: {len(singly_linked_list)}')

singly_linked_list.insert(0, -10)
print(f'List after insert item = -10 in index = 0: {singly_linked_list}, size: {len(singly_linked_list)}')
singly_linked_list.insert(5, -10)
print(f'List after insert item = -10 in index = 5: {singly_linked_list}, size: {len(singly_linked_list)}')
singly_linked_list.insert(3, 100)
print(f'List after insert item = 100 in index = 3: {singly_linked_list}, size: {len(singly_linked_list)}')

print(f'List[3] = {singly_linked_list[6]}')
singly_linked_list[0] = -50
print(f'List after list[0] = -50: {singly_linked_list}, size: {len(singly_linked_list)}')
singly_linked_list.__delitem__(0)
print(f'List after delete list[0]: {singly_linked_list}, size: {len(singly_linked_list)}')

singly_linked_list.delete_by_value(-10)
print(f'List after delete item = -10: {singly_linked_list}, size: {len(singly_linked_list)}')
