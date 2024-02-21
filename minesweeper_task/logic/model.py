import json
import random
from collections import deque

from minesweeper_task.logic.terms import Terms
from minesweeper_task.logic.field import Field
from minesweeper_task.logic.players import Players


class Model:
    def __init__(self):
        self.__width = None
        self.__height = None
        self.__mines_count = None

        self.__fields = None
        self.__mine_fields = None

        self.__flags_count = None
        self.__remaining_mines_count = None

    def init_game_data(self, width, height, mines_count):
        self.__width = width
        self.__height = height

        self.__mines_count = mines_count
        self.__remaining_mines_count = mines_count

        self.__flags_count = 0
        current_mines_count = 0

        self.__fields = [[Field() for _ in range(self.__height)] for _ in range(self.__width)]

        while current_mines_count < self.__mines_count:
            i = random.randint(0, self.__width - 1)
            j = random.randint(0, self.__height - 1)

            if self.__fields[i][j].data == -1:
                continue

            self.__fields[i][j].data = Terms.MINE
            current_mines_count += 1

        for x in range(self.__width):
            for y in range(self.__height):
                if self.__fields[x][y].data == 0:
                    current_mines_count = 0

                    for i in range(3):
                        index_i = x - 1 + i

                        if index_i < 0 or index_i >= self.__width:
                            continue

                        for j in range(3):
                            index_j = y - 1 + j

                            if index_j < 0 or index_j >= self.__height:
                                continue

                            if i == 1 and j == 1:
                                continue

                            if self.__fields[index_i][index_j].data == Terms.MINE:
                                current_mines_count += 1

                    self.__fields[x][y].data = current_mines_count

    def __find_has_no_mine_fields(self, x, y):
        fields_for_opening = {(x, y): self.__fields[x][y].data}
        fields_deque = deque()
        fields_deque.appendleft((x, y))

        while fields_deque:
            current_x, current_y = fields_deque.pop()

            for i in range(3):
                index_i = current_x - 1 + i

                if index_i < 0 or index_i >= self.__width:
                    continue

                for j in range(3):
                    index_j = current_y - 1 + j

                    if index_j < 0 or index_j >= self.__height:
                        continue

                    if self.__fields[index_i][index_j].data == Terms.MINE or self.__fields[index_i][index_j].is_flag:
                        continue

                    if 1 <= self.__fields[index_i][index_j].data <= 8:
                        if (index_i, index_j) in fields_for_opening:
                            continue

                    if self.__fields[index_i][index_j].data == 0:
                        if (index_i, index_j) in fields_for_opening:
                            continue

                        fields_deque.appendleft((index_i, index_j))

                    fields_for_opening[(index_i, index_j)] = self.__fields[index_i][index_j].data

        return fields_for_opening

    def check_field(self, x, y):
        if self.__fields[x][y].data == Terms.MINE:
            return {Terms.GAME_OVER: self.__fields}

        if self.__fields[x][y].data == 0:
            return self.__find_has_no_mine_fields(x, y)

        return {(x, y): self.__fields[x][y].data}

    def set_flag(self, x, y):
        if self.__fields[x][y].is_flag:

            if self.__fields[x][y] == Terms.MINE:
                self.__remaining_mines_count += 1

            self.__flags_count -= 1
            self.__fields[x][y].is_flag = False

            return Terms.FLAG_OFF

        if self.__flags_count == self.__mines_count:
            return

        if self.__fields[x][y].data == Terms.MINE:
            self.__remaining_mines_count -= 1

            if self.__remaining_mines_count == 0:
                return Terms.WIN

        self.__flags_count += 1
        self.__fields[x][y].is_flag = True

        return Terms.FLAG_ON

    @staticmethod
    def add_player(name, time):
        Players(name, time).add_player()

    @staticmethod
    def load_scores():
        return Players.load_scores()

    def pushed_center_click(self, x, y):
        neighbors_field = []

        for i in range(3):
            for j in range(3):
                if i != 1 and j != 1:
                    neighbor_x = x - 1 + i
                    index_j = y - 1 + j

                    if neighbor_x < 0 or index_j < 0 or neighbor_x >= self.__width or index_j >= self.__height:
                        continue

                    neighbors_field.append((neighbor_x, index_j))

        return neighbors_field
