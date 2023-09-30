from hash_table_task.hash_table import HashTable

hash_table = HashTable(800)
hash_table.add(-2)
hash_table.add('5')
hash_table.add('abc')
hash_table.add(100)
hash_table.add(-99)
hash_table.add(16)
hash_table.add('16')

value = 100
print(f'{value} in hash table:...{value in hash_table}')

print(hash_table)
hash_table.delete(100)
print(hash_table)
hash_table.delete(-100)
print(hash_table)

iterator = hash_table.__iter__()
for item in iterator:
    print('%s' % item, end=' ')
