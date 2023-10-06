import json
import random


class Model:
    def __init__(self):
        self.__size_x = None
        self.__size_y = None
        self.__mines_count = None
        self.__field = None
        self.__minefields = None
        self.__fields_for_opening = None
        self.__flags_count = None
        self.__remaining_mines_count = None

    def create_game_field(self, size_x, size_y, mines_count):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__mines_count = mines_count
        self.__minefields = []
        self.__flags_count = 0
        self.__fields_for_opening = dict()
        self.__remaining_mines_count = mines_count
        self.__field = [[0 for _ in range(self.__size_y)] for _ in range(self.__size_x)]
        current_mines_count = 0

        while current_mines_count < self.__mines_count:
            i = random.randint(0, self.__size_x - 1)
            j = random.randint(0, self.__size_y - 1)

            if self.__field[i][j] == -1:
                continue

            self.__field[i][j] = -1
            self.__minefields.append((i, j))
            current_mines_count += 1

        for x in range(self.__size_x):
            for y in range(self.__size_y):
                if self.__field[x][y] == 0:
                    current_mines_count = 0

                    for i in range(3):
                        for j in range(3):
                            if i == 1 and j == 1:
                                continue

                            index_i = x - 1 + i
                            index_j = y - 1 + j

                            if index_i < 0 or index_j < 0 or index_i >= self.__size_x or index_j >= self.__size_y:
                                continue

                            if self.__field[index_i][index_j] == -1:
                                current_mines_count += 1

                    self.__field[x][y] = current_mines_count

    def __find_fields_for_opening(self, x, y):
        for i in range(3):
            for j in range(3):
                index_i = x - 1 + i
                index_j = y - 1 + j

                if index_i < 0 or index_j < 0 or index_i >= self.__size_x or index_j >= self.__size_y:
                    continue

                if self.__field[index_i][index_j] == -1:
                    continue

                if 1 <= self.__field[index_i][index_j] <= 8:
                    self.__fields_for_opening[(index_i, index_j)] = self.__field[index_i][index_j]
                    continue

                if self.__field[index_i][index_j] == 0:
                    self.__fields_for_opening[(index_i, index_j)] = None
                    # TODO здесь вызвать рекурсивно, но код падает из-за превышения глубины

    def pushed_left_click(self, x, y):
        if isinstance(self.__field[x][y], str):
            self.__field[x][y] = int(self.__field[x][y])

            if self.__field[x][y] == -1:
                self.__remaining_mines_count += 1

            self.__flags_count -= 1

            return -2, self.__field[x][y]

        if self.__field[x][y] == -1:
            return -1, self.__minefields

        if self.__field[x][y] == 0:
            self.__fields_for_opening[(x, y)] = None
            self.__find_fields_for_opening(x, y)

            return 0, self.__fields_for_opening

        return 1, self.__field[x][y]

    def put_flag(self, x, y):
        if self.__field[x][y] == -1:
            self.__remaining_mines_count -= 1

        if self.__remaining_mines_count == 0 and self.__flags_count == self.__mines_count:
            return 1

        self.__flags_count += 1
        self.__field[x][y] = str(self.__field[x][y])
        return 0

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
