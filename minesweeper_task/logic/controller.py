class Controller:
    def __init__(self, view, model):
        self.__model = model
        self.__view = view

    def prepare(self, size_x=9, size_y=9, mines_count=10):
        game_field = self.__model.create_game_field(size_x, size_y, mines_count)
        self.__view.add_widgets_on_game_field(game_field, size_x, size_y)

    def pushed_left_click(self, x, y):
        self.__model.pushed_left_click(x, y)

    def pushed_right_click(self, x, y):
        self.__model.set_flag(x, y)

    def game_over(self, minefields):
        self.__view.show_all_manes_and_game_over(minefields)

    def remove_flag(self, data, x, y):
        self.__view.hide_flag(data, x, y)

    def set_flag(self, x, y):
        self.__view.show_flag(x, y)
