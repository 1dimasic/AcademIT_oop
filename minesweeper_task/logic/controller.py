import time
from minesweeper_task.logic.terms import Terms



class Controller:
    def __init__(self, view, model):
        self.__model = model
        self.__view = view
        self.__start_time = None

    def start(self, rows=10, columns=10, mines=50):
        try:
            width = int(rows)
            height = int(columns)
        except ValueError:
            return False, 'Некорректный тип данных'

        try:
            mines_count = int(mines)
        except ValueError:
            return False, 'Некорректный тип данных'

        if width <= 0 or width > 15 or height <= 0 or height > 15:
            return False, 'Размеры поля должны быть от 5 до 15'

        if mines_count <= 0:
            return False, 'Количество мин должно быть больше 0'

        if mines_count > width * height * 0.8:
            return False, f'Количество мин должно быть меньше {int(width * height * 0.15)}'

        self.__model.init_game_data(width, height, mines_count)
        self.__view.init_game_field(width, height)
        self.__start_time = time.time()

        return True, ''

    def click_left(self, x, y):
        result = self.__model.check_field(x, y)

        if Terms.GAME_OVER in result:
            self.__view.show_mines_and_game_over(result[Terms.GAME_OVER])
            return

        self.__view.open_field(result)

    def click_right(self, x, y):
        result = self.__model.set_flag(x, y)

        if result == Terms.WIN:
            self.__view.show_flag(x, y)
            self.__view.show_winning_message(time.time() - self.__start_time)
            return

        if result == Terms.FLAG_ON:
            self.__view.show_flag(x, y)
            return

        self.__view.hide_flag(x, y)

    def pushed_center_click(self, x, y):
        neighbors_fields = self.__model.pushed_center_click(x, y)
        self.__view.f(neighbors_fields)

    def add_player(self, name, game_time):
        self.__model.add_player(name, game_time)

    def get_high_scores(self):
        return self.__model.load_scores()
