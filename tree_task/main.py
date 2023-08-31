from tree_task.tree import Tree

tree = Tree()
tree_list = [10, 7, 16, 5, 8, 14, 20, 4, 6, 7, 9, 13, 15, 21, 19]
tree_list1 = [10, 7, 16, 6, 8, 20]
for node in tree_list1:
    tree.add(node)

# tree.visiting_in_depth_with_recursion()
# print()
# tree.visiting_in_depth()
# print()
tree.visiting_in_width()
print()
tree.delete(16)
print()
tree.visiting_in_width()
