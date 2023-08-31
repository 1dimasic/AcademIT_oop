from tree_task.tree_node import TreeNode
from collections import deque


class Tree:
    def __init__(self):
        self.__root = None
        self.__count = 0

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
            if node.data < current_node.data:
                if current_node.left:
                    current_node = current_node.left
                    continue

                current_node.left = node
                self.__count += 1
                break

            else:
                if current_node.right:
                    current_node = current_node.right
                    continue

                current_node.right = node
                self.__count += 1
                break

    def visiting_in_depth_with_recursion(self, node=None):
        if not node:
            node = self.__root

        print(node, end=' ')
        children = node.left, node.right

        if all(child is None for child in children):
            return

        for child in children:
            if not child:
                continue

            self.visiting_in_depth_with_recursion(child)

    def visiting_in_depth(self):
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

    def visiting_in_width(self):
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

                return False

            else:
                if current_node.right:
                    parent_node = current_node
                    current_node = current_node.right
                    continue

                return False

    def delete(self, value):
        current_node, parent_node = self.find(value)

        if not current_node:
            return False

        children = current_node.left, current_node.right

        if all(child for child in children):
            return

        for child in children:
            if not child:
                continue

            if parent_node.left == current_node:
                parent_node.left = child

            else:
                parent_node.right = child

            return

        if parent_node.left == current_node:
            parent_node.left = None

        else:
            parent_node.right = None
