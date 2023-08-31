from hash_task.hash_table import HashTable

hash_table = HashTable(8)
hash_table.add(-2)
hash_table.add('5')
hash_table.add('abc')
hash_table.add(100)
hash_table.add(-99)
hash_table.add(16)
hash_table.add('16')

print(hash_table)
element = 10
print(f'Элемент {element} находит по адресу: {hash_table.find(element)}')
element = 'abc'
print(f'Элемент {element} находит по адресу: {hash_table.find(element)}')

iterator = hash_table.__iter__()
for item in iterator:
    print(item, end=' ')
