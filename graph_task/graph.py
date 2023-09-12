from collections import deque


class Graph:
    def __init__(self, graph):
        if not isinstance(graph, list):
            raise TypeError(f'Incorrect type of argument "{type(graph).__name__}", not list')

        if not all(isinstance(item, int) for row in graph for item in row):
            raise TypeError(f'Incorrect type for graph item, not int')

        self.__graph = graph
        self.__count = len(graph)

    def visit_in_width(self, function=None):
        visited = [False] * self.__count

        graph_deque = deque()
        graph_deque.appendleft(0)

        while graph_deque:
            key = False

            if visited[vertex := graph_deque.pop()]:
                continue

            try:
                function(self.__graph[vertex][vertex])
            except TypeError:
                pass

            visited[vertex] = True

            for i in range(self.__count):
                if vertex == i:
                    continue

                if self.__graph[vertex][i] == 1 and not visited[i]:
                    graph_deque.appendleft(i)
                    key = True
                    continue

            if not key:
                try:
                    new_vertex = visited.index(False)
                    graph_deque.appendleft(new_vertex)
                except ValueError:
                    return

    def visit_in_depth(self, function=None):
        visited = [False] * self.__count
        graph_deque = deque()
        graph_deque.appendleft(0)

        while graph_deque:
            key = False

            if visited[vertex := graph_deque.popleft()]:
                continue

            try:
                function(self.__graph[vertex][vertex])
            except TypeError:
                pass

            visited[vertex] = True

            for i in range(self.__count - 1, -1, -1):
                key = False

                if vertex == i:
                    continue

                if self.__graph[vertex][i] == 1 and not visited[i]:
                    graph_deque.appendleft(i)
                    key = True
                    continue

            if not key and not graph_deque:
                try:
                    new_vertex = visited.index(False)
                    graph_deque.appendleft(new_vertex)
                except ValueError:
                    return

    def visit_in_depth_with_recursion(self, vertex, visited=None, function=None):
        if visited is None:
            visited = [False] * self.__count

        try:
            function(self.__graph[vertex][vertex])
        except TypeError:
            pass

        visited[vertex] = True

        for i in range(self.__count):
            if i == vertex:
                continue

            if self.__graph[vertex][i] == 1 and not visited[i]:
                self.visit_in_depth_with_recursion(i, visited, function=function)

        try:
            new_vertex = visited.index(False)
            self.visit_in_depth_with_recursion(new_vertex, visited, function=function)
        except ValueError:
            return

        return
