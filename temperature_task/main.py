from temperature_task.controller import Controller
from temperature_task.converter import Converter
from temperature_task.view import View

converter = Converter()
view = View()
controller = Controller(converter, view)
view.set_controller(controller)
view.start()
