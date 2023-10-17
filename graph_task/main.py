from graph_task.graph import Graph

graph_matrix = [[0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0]]

graph = Graph(graph_matrix)

print('Visit in width:', end=' ')
graph.visit_in_width(lambda e: print(e, end=' '))
print()

print('Visit in depth:', end=' ')
graph.visit_in_depth(lambda e: print(e, end=' '))
print()

print('Visit in depth with recursion:', end=' ')
graph.visit_in_depth_with_recursion(lambda e: print(e, end=' '))
