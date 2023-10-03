from array_list_task.array_list import ArrayList

array_list_1 = ArrayList(6)
array_list_1.append(5)
array_list_1.append(8)
array_list_1.append(8)
array_list_1.append(-3)
array_list_1.append(-3)
array_list_1.append(8)
array_list_1.append(0)
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')

print(f'Array list[-6: -1]: {array_list_1[slice(-6, -1)]}')
print(f'array_list_1[1] = {array_list_1[1]}')
array_list_1[3] = -50
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')
array_list_1.__delitem__(3)
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')

array_list_1.insert(6, 10)
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')

array_list_2 = ArrayList()
array_list_2.append(1)
array_list_2.append(-1)
array_list_1.extend(array_list_2)
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')

array_list_1.pop()
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')
array_list_1.pop(2)
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')
array_list_1.remove(5)
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')

array_list_1 += array_list_2
print(f'Array list: {array_list_1}, size: {len(array_list_1)}')
print(f'Value 10 in array list: {array_list_1}....{10 in array_list_1}')
print(f'Value -8 in array list: {array_list_1}.....{-8 in array_list_1}')

iterator = array_list_1.__iter__()
try:
    while True:
        print(iterator.__next__())
except StopIteration:
    pass

iterator = array_list_1.__reversed__()
try:
    while True:
        print(iterator.__next__())
except StopIteration:
    pass

print(f'Value {array_list_1[2]} index = {array_list_1.index(8, 2)}')

print(f'Value {array_list_1[2]} count = {array_list_1.count(array_list_1[2])}')
print(f'Value 100 count = {array_list_1.count(100)}')

array_list_1.reverse()
print(f'Reverse array list: {array_list_1}')
