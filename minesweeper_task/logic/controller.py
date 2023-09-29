class Controller:
    def __init__(self, view, model):
        self.__model = model
        self.__view = view

    def prepare(self, size_x=9, size_y=9, mines_count=10):
        game_field = self.__model.create_game_field(size_x, size_y, mines_count)
        self.__view.add_widgets_on_game_field(game_field, size_x, size_y)

    def play(self, x, y):
        self.__model.play(x, y)
