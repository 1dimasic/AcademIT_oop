from tree_task.tree_node import TreeNode
from collections import deque


class Tree:
    def __init__(self, function=None):
        self.__root = None
        self.__count = 0
        self.__function = function

    def __len__(self):
        return self.__count

    def add(self, data):
        node = TreeNode(data)

        if not self.__count:
            self.__root = node
            self.__count += 1
            return

        current_node = self.__root

        while True:
            if self.compare(node.data, current_node.data):
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

    def visit_in_depth_with_recursion(self, node=None, function=None):
        if self.__count == 0:
            return

        if not node:
            node = self.__root

        if not isinstance(node, TreeNode):
            raise TypeError(f'Incorrect type of arguments "{type(node).__name__}"')

        try:
            function(node)
        except TypeError:
            pass

        children = node.left, node.right

        if all(not child for child in children):
            return

        for child in children:
            if not child:
                continue

            self.visit_in_depth_with_recursion(child)

    def visit_in_depth(self, function=None):
        if self.__count == 0:
            return

        tree_deque = deque()
        tree_deque.append(self.__root)

        while tree_deque:
            node = tree_deque.popleft()

            try:
                function(node)
            except TypeError:
                pass

            children = node.right, node.left

            for child in children:
                if not child:
                    continue

                tree_deque.appendleft(child)

    def visit_in_width(self, function=None):
        if self.__count == 0:
            return

        tree_deque = deque()
        tree_deque.append(self.__root)

        while tree_deque:
            node = tree_deque.pop()

            try:
                function(node)
            except TypeError:
                pass

            children = node.left, node.right

            for child in children:
                if not child:
                    continue

                tree_deque.appendleft(child)

    def find(self, data):
        parent_node = None
        current_node = self.__root

        while True:
            if self.__function:
                if self.__function(current_node.data) == self.__function(data):
                    return current_node, parent_node
            else:
                if current_node.data == data:
                    return current_node, parent_node

            if self.compare(data, current_node.data):
                if current_node.left:
                    parent_node = current_node
                    current_node = current_node.left
                    continue

            else:
                if current_node.right:
                    parent_node = current_node
                    current_node = current_node.right
                    continue

            return False

    def delete(self, data):
        try:
            current_node, parent_node = self.find(data)
        except TypeError:
            return False

        # удаляем лист
        if not current_node.left and not current_node.right:
            try:
                # удаляемый лист это левый ребенок
                if parent_node.left == current_node:
                    parent_node.left = None
                else:
                    # удаляемый лист это правый ребенок
                    parent_node.right = None

                self.__count -= 1

                return True

            except AttributeError:
                # удаляемый лист это корень
                self.__root = None
                self.__count = 0

                return True

        # удаляем корень с одним ребенком
        if current_node == self.__root and (not current_node.left or not current_node.right):
            self.__root = current_node.left if current_node.left else current_node.right
            current_node.left = None
            current_node.right = None
            self.__count -= 1

            return True

        # удаляем не корневой узел с одним ребенком
        if current_node.left and not current_node.right or not current_node.left and current_node.right:
            child = current_node.left if current_node.left else current_node.right

            if self.compare(current_node.data, parent_node.data):
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

            if not parent_node:
                self.__root = next_node
                self.__count -= 1

                return True

            if self.compare(current_node.data, parent_node.data):
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
            if self.compare(current_node.data, parent_node.data):
                parent_node.left = next_node
            else:
                parent_node.right = next_node

        else:
            self.__root = next_node

        next_node.left = current_node.left
        next_node.right = current_node.right

        return True

    def compare(self, node_1, node_2) -> bool:
        if self.__function:
            if self.__function(node_1) < self.__function(node_2):
                return True
            else:
                return False
        else:
            if node_1 < node_2:
                return True
            else:
                return False

    def __contains__(self, item):
        try:
            if self.find(item)[0]:
                return True
        except TypeError:
            return False
