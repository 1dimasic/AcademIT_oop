from graph_task.graph import Graph

graf_matrix = [[0, 1, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 1, 0]]

graf = Graph(graf_matrix)

print('Visit in width:', end=' ')
graf.visit_in_width(print)
print()

print('Visit in depth:', end=' ')
graf.visit_in_depth(print)
print()

print('Visit in depth with recursion:', end=' ')
graf.visit_in_depth_with_recursion(print)
