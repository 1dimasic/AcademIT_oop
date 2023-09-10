from graph_task.graph import Graph

graf_list = [[0, 0, 0, 0, 0, 1, 0], [0, 10, 0, 0, 0, 1, 1], [0, 0, 20, 0, 0, 1, 0], [0, 0, 0, 30, 1, 1, 0],
             [0, 0, 0, 1, 40, 0, 0], [1, 1, 1, 1, 0, 50, 0], [0, 1, 0, 0, 0, 0, 60]]

graf = Graph(graf_list)
graf.visit_2()
