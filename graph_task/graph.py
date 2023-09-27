from collections import deque


class Graph:
    def __init__(self, graph_matrix):
        if not isinstance(graph_matrix, list):
            raise TypeError(f'Incorrect type of argument "{type(graph_matrix).__name__}", not list')

        if not all(isinstance(row, list) for row in graph_matrix):
            raise TypeError(f'Incorrect type, must be list')

        max_size = len(max((row for row in graph_matrix), key=len))
        min_size = len(min((row for row in graph_matrix), key=len))

        if max_size != min_size or max_size != len(graph_matrix):
            raise ValueError(f'Graph matrix must be square size')

        if not all(isinstance(item, int) for row in graph_matrix for item in row):
            raise TypeError(f'Incorrect type for matrix item, not int')

        self.__graph_matrix = graph_matrix
        self.__count = len(graph_matrix)

    def visit_in_width(self, function):
        visited = [False] * self.__count
        graph_deque = deque()

        while any(not visit for visit in visited):
            vertex = visited.index(False)
            graph_deque.appendleft(vertex)

            while len(graph_deque) != 0:
                vertex = graph_deque.pop()

                if visited[vertex]:
                    continue

                function(vertex, end=' ')
                visited[vertex] = True

                for i in range(self.__count):
                    if vertex == i:
                        continue

                    if self.__graph_matrix[vertex][i] == 1 and not visited[i]:
                        graph_deque.appendleft(i)

    def visit_in_depth(self, function):
        visited = [False] * self.__count
        graph_deque = deque()

        while any(not visit for visit in visited):
            vertex = visited.index(False)
            graph_deque.appendleft(vertex)

            while len(graph_deque) != 0:
                vertex = graph_deque.popleft()

                if visited[vertex]:
                    continue

                function(vertex, end=' ')
                visited[vertex] = True

                for i in range(self.__count - 1, -1, -1):
                    if vertex == i:
                        continue

                    if self.__graph_matrix[vertex][i] == 1 and not visited[i]:
                        graph_deque.appendleft(i)

    def __visit_in_depth_with_recursion(self, vertex, visited, function):
        function(vertex, end=' ')
        visited[vertex] = True

        for i in range(self.__count):
            if i == vertex:
                continue

            if self.__graph_matrix[vertex][i] == 1 and not visited[i]:
                self.__visit_in_depth_with_recursion(i, visited, function)

        try:
            new_vertex = visited.index(False)
            self.__visit_in_depth_with_recursion(new_vertex, visited, function)
        except ValueError:
            return

    def visit_in_depth_with_recursion(self, function):
        visited = [False] * self.__count
        vertex = 0

        self.__visit_in_depth_with_recursion(vertex, visited, function)
