import random


class Model:
    def __init__(self):
        self.__size_x = None
        self.__size_y = None
        self.__mines_count = None
        self.__field = None

    def create_game_field(self, size_x, size_y, mines_count):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__mines_count = mines_count
        self.__field = [[0 for _ in range(self.__size_y)] for _ in range(self.__size_x)]
        current_mines_count = 0

        while current_mines_count < self.__mines_count:
            i = random.randint(0, self.__size_x - 1)
            j = random.randint(0, self.__size_y - 1)

            if self.__field[i][j] == -1:
                continue

            self.__field[i][j] = -1
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

        return self.__field

    def play(self, x, y):
        if self.__field[x][y] == -1:
            return -1

    def play_1(self, x, y):
        if self.__field[x][y] == 0:
            print('0')
