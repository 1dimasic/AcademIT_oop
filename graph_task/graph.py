from collections import deque


class Graph:
    def __init__(self, graph):
        if not isinstance(graph, list):
            raise TypeError

        self.graph = graph
        self.__count = len(graph)

    def visit(self):
        visited = [False] * self.__count
        graph_deque = deque()
        graph_deque.appendleft(0)

        while graph_deque:
            if visited[graph_deque[-1]]:
                graph_deque.pop()
                continue

            print(self.graph[graph_deque[-1]][graph_deque[-1]], end=' ')
            visited[graph_deque[-1]] = True

            for i in range(self.__count):
                if graph_deque[-1] == i:
                    continue

                if self.graph[graph_deque[-1]][i] == 1:
                    graph_deque.appendleft(i)

    def visit_1(self):
        visited = [False] * self.__count
        graph_deque = deque()
        graph_deque.appendleft(0)

        while graph_deque:
            print(self.graph[graph_deque[0]][graph_deque[0]], end=' ')
            index = graph_deque[0]
            visited[index] = True
            graph_deque.popleft()

            for i in range(self.__count - 1, -1, -1):
                if index == i:
                    continue

                if self.graph[index][i] == 1 and not visited[i]:
                    graph_deque.appendleft(i)

    def visit_2(self, peak=None, v=[False] * 6):
        if not peak:
            peak = 0

        if v[peak]:
            return

        print(self.graph[peak][peak])

        for i in range(self.__count):
            if self.graph[peak][i] == 1:

                self.visit_2(i)
