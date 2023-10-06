import time


class Controller:
    def __init__(self, view, model):
        self.__model = model
        self.__view = view
        self.__start_time = None

    def start(self, size_x=9, size_y=9, mines_count=10):
        if mines_count > size_x * size_y:
            raise ValueError(f'Mines count must be <= {size_x*size_y}, not {mines_count}')

        self.__model.create_game_field(size_x, size_y, mines_count)
        self.__view.add_fields(size_x, size_y)
        self.__start_time = time.time()

    def pushed_left_click(self, x, y):
        result = self.__model.pushed_left_click(x, y)

        if result[0] == -2:
            self.__view.put_away_flag(x, y, result[1])

        if result[0] == -1:
            self.__view.show_all_mines_and_game_over(result[1])

        if result[0] == 0:
            self.__view.open_field(result[1])

        if result[0] == 1:
            self.__view.open_field(x, y, result[1])

    def pushed_right_click(self, x, y):
        result = self.__model.put_flag(x, y)

        if result == 1:
            self.__view.show_winning_message(time.time() - self.__start_time)

        if result == 0:
            self.__view.put_flag(x, y)

    def add_to_high_scores(self, name_and_time):
        self.__model.add_to_high_scores(name_and_time)

    def load_high_scores(self):
        return self.__model.load_high_scores()
