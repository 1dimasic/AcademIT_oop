from tree_task.tree_node import TreeNode
from collections import deque


class Tree:
    def __init__(self):
        self.__root = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def add(self, data):
        if not isinstance(data, int | float):
            raise TypeError(f'Incorrect type of arguments "{type(data).__name__}"')

        node = TreeNode(data)

        if not self.__count:
            self.__root = node
            self.__count += 1
            return

        current_node = self.__root

        while True:
            if node < current_node:
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
            break

    def iterative_deepening_depth_first_search(self, node=None):
        if not node:
            node = self.__root

        if not isinstance(node, TreeNode):
            raise TypeError(f'Incorrect type of arguments "{type(node).__name__}"')

        print(node, end=' ')
        children = node.left, node.right

        if all(not child for child in children):
            return

        for child in children:
            if not child:
                continue

            self.iterative_deepening_depth_first_search(child)

    def depth_first_search(self):
        tree_deque = deque()
        tree_deque.append(self.__root)

        while tree_deque:
            print(tree_deque[0], end=' ')

            children = tree_deque[0].right, tree_deque[0].left
            tree_deque.popleft()

            for child in children:
                if not child:
                    continue

                tree_deque.appendleft(child)

    def breadth_first_search(self):
        tree_deque = deque()
        tree_deque.append(self.__root)

        while tree_deque:
            print(tree_deque[-1], end=' ')

            children = tree_deque[-1].left, tree_deque[-1].right
            tree_deque.pop()

            for child in children:
                if not child:
                    continue

                tree_deque.appendleft(child)

    def find(self, value):
        if not isinstance(value, int | float):
            raise TypeError(f'Incorrect type of arguments "{type(value).__name__}"')

        parent_node = self.__root
        current_node = self.__root

        while True:
            if current_node.data == value:
                return current_node, parent_node

            if value < current_node.data:
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

    def delete(self, value):
        if not isinstance(value, int | float):
            raise TypeError(f'Incorrect type of arguments "{type(value).__name__}"')

        try:
            current_node, parent_node = self.find(value)
        except TypeError:
            return False

        children = current_node.left, current_node.right

        # удаляемый узел имеет 2 ребенка
        if all(child for child in children):
            node = current_node.right
            previous_node = current_node.right

            while node.left:
                if node == previous_node:
                    node = node.left

                else:
                    node = node.left
                    previous_node = previous_node.left

            # если удаляем корень
            if current_node == self.__root and parent_node == self.__root:
                if node.right:
                    previous_node.left = node.right
                    node.left = current_node.left
                    node.right = current_node.right
                    self.__root = node

                else:
                    previous_node.left = None
                    node.left = current_node.left
                    node.right = current_node.right
                    self.__root = node

                return

                # если правое поддерево имеет только один узел
            if node is previous_node:
                node.left = current_node.left

                if parent_node > current_node:
                    parent_node.left = node

                else:
                    parent_node.right = node

                current_node.left = None
                current_node.right = None

                return

            # самый левый элемент в правом поддереве не имеет правого ребенка
            if not node.right:
                previous_node.left = None
                if parent_node > current_node:
                    parent_node.left = node
                else:
                    parent_node.right = node

                node.right = previous_node
                node.left = current_node.left

                return

            # самый левый элемент в правом поддереве имеет правого ребенка
            previous_node.left = node.right

            if parent_node > current_node:
                node.right = None
                parent_node.left = node
            else:
                previous_node.left = node.right
                node.right = None
                parent_node.right = node

            node.left = current_node.left
            node.right = current_node.right

            return

        # удаление узла с одним ребенком
        for child in children:
            if not child:
                continue

            if parent_node.left == current_node:
                parent_node.left = child

            else:
                parent_node.right = child

            return

        # удаление узла без детей
        if parent_node.left == current_node:
            parent_node.left = None

        else:
            parent_node.right = None
