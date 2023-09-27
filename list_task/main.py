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
print(f'List copy: {singly_linked_list_copy}, size: {len(singly_linked_list_copy)}')

index = 0
new_value = -10
singly_linked_list.insert(index, new_value)
print(f'List after insert item = {new_value} in index = {index}: {singly_linked_list}, size: {len(singly_linked_list)}')

index = 5
new_value = -10
singly_linked_list.insert(index, new_value)
print(f'List after insert item = {new_value} in index = {index}: {singly_linked_list}, size: {len(singly_linked_list)}')

index = 3
new_value = 100
singly_linked_list.insert(index, new_value)
print(f'List after insert item = {new_value} in index = {index}: {singly_linked_list}, size: {len(singly_linked_list)}')

index = 3
print(f'List[{index}] = {singly_linked_list[3]}')

index = 0
new_value = -50
singly_linked_list[index] = new_value
print(f'List after list[{index}] = {new_value}: {singly_linked_list}, size: {len(singly_linked_list)}')

index = 0
singly_linked_list.__delitem__(index)
print(f'List after delete list[{index}]: {singly_linked_list}, size: {len(singly_linked_list)}')

deleted_value = -10
singly_linked_list.delete_by_value(deleted_value)
print(f'List after delete item = {deleted_value}: {singly_linked_list}, size: {len(singly_linked_list)}')
