class Controller:
    def __init__(self, converter, view):
        self.__converter = converter
        self.__view = view

    def convert_temperature(self, input_temperature, input_scale):
        output_temperature = self.__converter.convert(input_temperature, input_scale)
        self.__view.show(output_temperature)
