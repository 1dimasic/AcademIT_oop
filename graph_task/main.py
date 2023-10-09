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

print('Visit in width:')
graf.visit_in_width(print)
print()

print('Visit in depth:')
graf.visit_in_depth(print)
print()

print('Visit in depth with recursion:')
graf.visit_in_depth_with_recursion(print)
