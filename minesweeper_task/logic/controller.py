import time
from minesweeper_task.logic.terms import Terms


class Controller:
    def __init__(self, view, model):
        self.__model = model
        self.__view = view
        self.__start_time = None

    def start(self, width=9, height=9, mines_count=10):
        if width <= 0:
            raise ValueError(f'Invalid value = {width}, must be > 0')

        if height <= 0:
            raise ValueError(f'Invalid value = {height}, must be > 0')

        if mines_count <= 0:
            raise ValueError(f'Invalid value = {mines_count}, must be > 0')

        if mines_count > width * height * 0.15:
            raise ValueError(f'Invalid value = {mines_count}, must be <= {width * height * 0.15}')

        # TODO
        a = self.__model.create_game_field(width, height, mines_count)
        self.__view.add_fields(width, height, a)
        self.__start_time = time.time()

    def pushed_left_click(self, x, y):
        result = self.__model.pushed_left_click(x, y)

        if result[0] == Terms.MINE:
            self.__view.show_all_mines_and_game_over(result[1])

        if result[0] == Terms.EMPTY_FIELD:
            self.__view.open_field(result[1])

        if result[0] == Terms.NOT_EMPTY_FIELD:
            self.__view.open_field(x, y, result[1])

    def pushed_right_click(self, x, y):
        result = self.__model.pushed_right_click(x, y)

        if result == 1:
            self.__view.put_flag(x, y)

        if result == Terms.WIN:
            self.__view.show_winning_message(time.time() - self.__start_time)

        if result == -2:
            self.__view.put_away_flag(x, y)

    def add_to_high_scores(self, name_and_time):
        self.__model.add_to_high_scores(name_and_time)

    def load_high_scores(self):
        return self.__model.load_high_scores()
