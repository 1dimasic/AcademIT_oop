import json
import random
from collections import deque
from minesweeper_task.logic.terms import Terms


class Model:
    def __init__(self):
        self.__width = None
        self.__height = None
        self.__mines_count = None
        self.__field = None
        self.__minefields = None
        self.__flags_count = None
        self.__remaining_mines_count = None

    def create_game_field(self, width, height, mines_count):
        self.__width = width
        self.__height = height
        self.__mines_count = mines_count
        self.__minefields = []
        self.__flags_count = 0
        self.__remaining_mines_count = mines_count
        self.__field = [[0 for _ in range(self.__height)] for _ in range(self.__width)]
        current_mines_count = 0

        while current_mines_count < self.__mines_count:
            i = random.randint(0, self.__width - 1)
            j = random.randint(0, self.__height - 1)

            if self.__field[i][j] == -1:
                continue

            self.__field[i][j] = -1
            self.__minefields.append((i, j))
            current_mines_count += 1

        for x in range(self.__width):
            for y in range(self.__height):
                if self.__field[x][y] == 0:
                    current_mines_count = 0

                    for i in range(3):
                        for j in range(3):
                            if i == 1 and j == 1:
                                continue

                            index_i = x - 1 + i
                            index_j = y - 1 + j

                            if index_i < 0 or index_j < 0 or index_i >= self.__width or index_j >= self.__height:
                                continue

                            if self.__field[index_i][index_j] == -1:
                                current_mines_count += 1

                    self.__field[x][y] = current_mines_count
        # TODO
        return self.__field

    def pushed_left_click(self, x, y):
        if self.__field[x][y] == Terms.MINE:
            return Terms.MINE, self.__minefields

        if self.__field[x][y] == Terms.EMPTY_FIELD:
            a = self.__find_fields_for_opening(x, y)
            return Terms.EMPTY_FIELD, a

        return Terms.NOT_EMPTY_FIELD, self.__field[x][y]

    def pushed_right_click(self, x, y):
        # TODO Документирующий комментарий
        if self.__field[x][y] == Terms.MINE:
            self.__remaining_mines_count -= 1

            if self.__remaining_mines_count == 0 and self.__flags_count == self.__mines_count:
                return Terms.WIN

            return 1

        if isinstance(self.__field[x][y], str):
            self.__field[x][y] = int(self.__field[x][y])

            if self.__field[x][y] == -1:
                self.__remaining_mines_count += 1

            self.__flags_count -= 1

            return -2

        self.__flags_count += 1
        self.__field[x][y] = str(self.__field[x][y])
        return 1

    @staticmethod
    def add_to_high_scores(name_and_time):
        with open('data/high_scores.json', 'r') as file:
            high_scores = json.load(file)
            high_scores.append(name_and_time)

        with open('data/high_scores.json', 'w') as file:
            json.dump(high_scores, file)

    @staticmethod
    def load_high_scores():
        with open('data/high_scores.json', 'r') as file:
            return json.load(file)

    def __find_fields_for_opening(self, coordinate_x, coordinate_y):
        fields_for_opening = {(coordinate_x, coordinate_y): None}
        fields_deque = deque()
        fields_deque.appendleft((coordinate_x, coordinate_y))

        while fields_deque:
            x, y = fields_deque.pop()

            for i in range(3):
                for j in range(3):
                    neighbor_x = x - 1 + i
                    neighbor_y = y - 1 + j

                    if neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= self.__width or neighbor_y >= self.__height:
                        continue

                    if self.__field[neighbor_x][neighbor_y] == -1:
                        continue

                    if 1 <= self.__field[neighbor_x][neighbor_y] <= 8:
                        if (neighbor_x, neighbor_y) in fields_for_opening:
                            continue

                        fields_for_opening[(neighbor_x, neighbor_y)] = self.__field[neighbor_x][neighbor_y]

                    if self.__field[neighbor_x][neighbor_y] == 0:
                        if (neighbor_x, neighbor_y) in fields_for_opening:
                            continue

                        fields_for_opening[(neighbor_x, neighbor_y)] = None
                        fields_deque.appendleft((neighbor_x, neighbor_y))

        return fields_for_opening
