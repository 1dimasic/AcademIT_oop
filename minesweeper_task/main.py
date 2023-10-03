from minesweeper_task.logic.controller import Controller
from minesweeper_task.gui.view import View
from minesweeper_task.logic.model import Model

model = Model()
view = View()
controller = Controller(view, model)
view.set_controller(controller)
model.set_controller(controller)
view.start()
