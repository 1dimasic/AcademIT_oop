from tree_task.tree import Tree

tree_1 = Tree()
tree_2 = Tree()

# tree_list_1 = [20, 15, 24, 7, 18, 21, 26, 5, 8, 16, 19, 21, 23, 25, 27, 17, 9]
tree_list_1 = [20, 15, 25, 16, 23]
# tree_list_1 = [20, 8, 25, 7, 18, 24, 28, 17, 19, 17, 26, 10,12]

for node in tree_list_1:
    tree_1.add(node)

# for node in tree_list_2:
#     tree_2.add(node)

# проверка обходов
# tree_1.breadth_first_search()
# print()
# tree_1.depth_first_search()
# print()
# tree_1.iterative_deepening_depth_first_search()
# print()

# проверка поиска
# node = 29
# try:
#     print(f'Элемент {node} находится в дереве?....', end='')
#     print(True if tree_1.find(node) else False)
# except TypeError:
#     pass
tree_1.breadth_first_search()
print()
# проверка удаления
nodes = []
for node in [15, 25, 23, 16, 20]:
    tree_1.delete_2(node)
    tree_1.breadth_first_search()
    nodes.append(node)
    print()
#
# print()

# node = 20
# tree_1.delete(node)
# tree_1.breadth_first_search()
# print()
