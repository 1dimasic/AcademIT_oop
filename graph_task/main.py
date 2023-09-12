from graph_task.graph import Graph

graf_list = [[-5, 1, 0, 0, 0, 0, 0, 0], [1, -1, 1, 1, 0, 0, 0, 0], [0, 1, 2, 0, 0, 1, 0, 0], [0, 1, 0, 6, 1, 0, 0, 0],
             [0, 0, 0, 1, 8, 0, 0, 0], [0, 0, 1, 0, 0, 11, 0, 0], [0, 0, 0, 0, 0, 0, 20, 1],
             [0, 0, 0, 0, 0, 0, 1, 30]]

graf = Graph(graf_list)

graf.visit_in_width(print)
print()
graf.visit_in_depth(print)
print()
graf.visit_in_depth_with_recursion(0, function=print)
