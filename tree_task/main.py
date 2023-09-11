import random
from tree_task.tree import Tree

tree_list_1 = [20, 15, 24, 7, 18, 21, 26, 5, 8, 16, 19, 21, 23, 25, 27, 17, 9]
tree_list_2 = ['a' * 8, 'a' * 5, 'a' * 10, 'a' * 3, 'a' * 6, 'a*9', 'a' * 12, 'a' * 4, 'a' * 8]
tree_list_3 = [20, 8, 25, 7, 18, 24, 28, 17, 19, 17, 26, 10, 12]

for i in range(10):
    tree = Tree()
    for node in tree_list_1:
        tree.add(node)

    nodes = tree_list_1[:]
    random.shuffle(nodes)

    for node in nodes:
        tree.delete(node)
        tree.visit_in_depth_with_recursion()

    print('%s:....%s' % (i, len(tree)))

for i in range(10):
    tree = Tree(len)
    for node in tree_list_2:
        tree.add(node)

    nodes = tree_list_2[:]
    random.shuffle(nodes)

    for node in nodes:
        tree.delete(node)
        tree.visit_in_width(function=len)

    print('%s:....%s' % (i, len(tree)))


tree = Tree()
for node in tree_list_1:
    tree.add(node)

print(f'18 in tree?.....{18 in tree}')
print(f'180 in tree?....{180 in tree}')