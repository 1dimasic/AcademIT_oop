from tree_task.tree import Tree

tree_1 = Tree()
tree_2 = Tree()

tree_list_1 = [20, 15, 24, 7, 18, 21, 26, 5, 8, 16, 19, 21, 23, 25, 27, 17, 9]
# tree_list_2 = [20, 15, 25, 10, 16, 23, 26, 24]

for node in tree_list_1:
    tree_1.add(node)

# for node in tree_list_2:
#     tree_2.add(node)

# проверка обходов
tree_1.breadth_first_search()
print()
tree_1.depth_first_search()
print()
tree_1.iterative_deepening_depth_first_search()
print()

# проверка поиска
node = 24
try:
    print(f'Элемент {node} находится в дереве?....', end='')
    print(True if tree_1.find(node) else False)
except TypeError:
    pass

# проверка удаления
node = 24
tree_1.delete(node)
tree_1.breadth_first_search()
print()

node = 20
tree_1.delete(node)
tree_1.breadth_first_search()
print()
