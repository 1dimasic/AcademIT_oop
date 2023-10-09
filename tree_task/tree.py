from tree_task.tree_node import TreeNode
from collections import deque


class Tree:
    def __init__(self, key_function=None):
        self.__root = None
        self.__count = 0
        self.__key_function = key_function

    def __len__(self):
        return self.__count

    def __equals(self, data_1, data_2):
        if self.__key_function:
            return self.__key_function(data_1) == self.__key_function(data_2)

        return data_1 == data_2

    def __is_less_than(self, data_1, data_2) -> bool:
        if self.__key_function:
            return self.__key_function(data_1) < self.__key_function(data_2)

        return data_1 < data_2

    def add(self, data):
        node = TreeNode(data)

        if self.__count == 0:
            self.__root = node
            self.__count += 1
            return

        current_node = self.__root

        while True:
            if self.__is_less_than(node.data, current_node.data):
                if current_node.left:
                    current_node = current_node.left
                    continue

                current_node.left = node
            else:
                if current_node.right:
                    current_node = current_node.right
                    continue

                current_node.right = node

            self.__count += 1
            return

    def visit_in_depth_with_recursion(self, function):
        if self.__count == 0:
            return

        self.__visit_in_depth_with_recursion(self.__root, function)

    def __visit_in_depth_with_recursion(self, node, function):
        function(node.data)
        children = node.left, node.right

        for child in children:
            if not child:
                continue

            self.__visit_in_depth_with_recursion(child, function)

    def visit_in_depth(self, function):
        if self.__count == 0:
            return

        tree_deque = deque()
        tree_deque.append(self.__root)

        while tree_deque:
            node = tree_deque.popleft()
            function(node.data)
            children = node.right, node.left

            for child in children:
                if not child:
                    continue

                tree_deque.appendleft(child)

    def visit_in_width(self, function):
        if self.__count == 0:
            return

        tree_deque = deque()
        tree_deque.append(self.__root)

        while tree_deque:
            node = tree_deque.pop()
            function(node.data)
            children = node.left, node.right

            for child in children:
                if not child:
                    continue

                tree_deque.appendleft(child)

    def __find(self, data):
        if self.__count == 0:
            return None, None

        parent_node = None
        current_node = self.__root

        while True:
            if self.__equals(current_node.data, data):
                return current_node, parent_node

            if self.__is_less_than(data, current_node.data):
                if current_node.left:
                    parent_node = current_node
                    current_node = current_node.left
                    continue
            else:
                if current_node.right:
                    parent_node = current_node
                    current_node = current_node.right
                    continue

            return None, None

    def delete(self, data):
        current_node, parent_node = self.__find(data)

        if not current_node:
            return False

        if not current_node.left and not current_node.right:
            # удаляем лист
            if current_node is self.__root:
                # удаляемый лист это корень
                self.__root = None
            elif self.__is_less_than(current_node.data, parent_node.data):
                # удаляемый лист это левый ребенок
                parent_node.left = None
            else:
                # удаляемый лист это правый ребенок
                parent_node.right = None

            self.__count -= 1
            return True

        if not current_node.left or not current_node.right:
            # удаляем узел с одним ребенком
            child = current_node.left if current_node.left else current_node.right

            if current_node is self.__root:
                # удаляемый узел это корень
                self.__root = child
                current_node.left = None
                current_node.right = None
                self.__count -= 1

                return True

            if self.__is_less_than(current_node.data, parent_node.data):
                parent_node.left = child
            else:
                parent_node.right = child

            current_node.left = None
            current_node.right = None
            self.__count -= 1

            return True

        # удаляем узел с двумя детьми
        next_node = current_node.right

        # если в правом поддереве удаляемого узла нет левого ребенка
        if not next_node.left:
            next_node.left = current_node.left
            current_node.right = None

            if parent_node is None:
                self.__root = next_node
                self.__count -= 1

                return True

            if self.__is_less_than(current_node.data, parent_node.data):
                parent_node.left = next_node
            else:
                parent_node.right = next_node

            self.__count -= 1

            return True

        # если в правом поддереве удаляемого узла есть левый ребенок
        previous_next = next_node
        next_node = next_node.left

        while next_node.left:
            next_node = next_node.left
            previous_next = previous_next.left

        if next_node.right:
            previous_next.left = next_node.right
        else:
            previous_next.left = None

        if parent_node:
            if self.__is_less_than(current_node.data, parent_node.data):
                parent_node.left = next_node
            else:
                parent_node.right = next_node
        else:
            self.__root = next_node

        next_node.left = current_node.left
        next_node.right = current_node.right
        self.__count -= 1

        return True

    def __contains__(self, item):
        return self.__find(item)[0]
