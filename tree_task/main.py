from tree_task.tree import Tree

tree_1 = Tree()
tree_2 = Tree()

tree_list_1 = [20, 15, 24, 7, 18, 21, 26, 5, 8, 16, 19, 20, 23, 25, 27, 17, 25, 9]
tree_list_2 = [20, 15, 25, 10, 16, 23, 26, 24]

for node in tree_list_1:
    tree_1.add(node)

for node in tree_list_2:
    tree_2.add(node)

tree_1.breadth_first_search()
print()
tree_1.depth_first_search()
print()
tree_1.iterative_deepening_depth_first_search()
print()

print(tree_1.find(25)[0])


