from collections import deque


class Graph:
    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError(f'Incorrect type of argument "{type(matrix).__name__}", not list')

        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f'Incorrect type of matrix row, must be list')

        row_max_size = len(max(matrix, key=len))
        row_min_size = len(min(matrix, key=len))

        if row_max_size != row_min_size or row_max_size != len(matrix):
            raise ValueError(f'Graph matrix must be square size')

        if not all(isinstance(item, int) for row in matrix for item in row):
            raise TypeError(f'Incorrect type for matrix item, not int')

        self.__matrix = matrix
        self.__count = len(matrix)

    def visit_in_width(self, function):
        visited = [False] * self.__count
        graph_deque = deque()

        for i in range(self.__count):
            if not visited[i]:
                graph_deque.appendleft(i)

            while len(graph_deque) != 0:
                vertex = graph_deque.pop()

                if visited[vertex]:
                    continue

                function(vertex)
                visited[vertex] = True

                for j in range(self.__count):
                    if vertex == j:
                        continue

                    if self.__matrix[vertex][j] == 1 and not visited[j]:
                        graph_deque.appendleft(j)

    def visit_in_depth(self, function):
        visited = [False] * self.__count
        graph_deque = deque()

        for i in range(self.__count):
            if not visited[i]:
                graph_deque.appendleft(i)

            while len(graph_deque) != 0:
                vertex = graph_deque.popleft()

                if visited[vertex]:
                    continue

                function(vertex)
                visited[vertex] = True

                for j in range(self.__count - 1, -1, -1):
                    if vertex == j:
                        continue

                    if self.__matrix[vertex][j] == 1 and not visited[j]:
                        graph_deque.appendleft(j)

    def __visit_in_depth_with_recursion(self, vertex, visited, function):
        function(vertex)
        visited[vertex] = True

        for i in range(self.__count):
            if i == vertex:
                continue

            if self.__matrix[vertex][i] == 1 and not visited[i]:
                self.__visit_in_depth_with_recursion(i, visited, function)

    def visit_in_depth_with_recursion(self, function):
        visited = [False] * self.__count

        for i in range(self.__count):
            if not visited[i]:
                self.__visit_in_depth_with_recursion(i, visited, function)
