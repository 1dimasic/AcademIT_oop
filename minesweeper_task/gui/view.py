import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

from minesweeper_task.logic.model import Model
from minesweeper_task.logic.field import Field


class View:
    def __init__(self):
        self.__root = Tk()
        self.__controller = None
        self.__size = 9
        self.__mines_count = 10
        self.__field_frame = None

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__root.geometry('300x300+400+100')
        self.__root.title('Minesweeper')
        self.__add_menu()
        self.__field_frame = ttk.Frame()
        self.__root.mainloop()

    def __add_menu(self):
        top = Menu(self.__root, tearoff=0)
        self.__root.config(menu=top)
        top.add_command(label='New game', command=self.__play)
        top.add_command(label='Settings', command=self.__show_game_settings)
        top.add_command(label='High scores', command=self.show_high_scores)
        top.add_command(label='About', command=self.show_about)
        top.add_command(label='Exit', command=sys.exit)

    @staticmethod
    def show_about():
        with open('data/about.dat', 'r') as file:
            showinfo(title='About', message=file.read())

    @staticmethod
    def show_high_scores():
        high_scores = Toplevel()
        high_scores.geometry('300x300+500+150')
        high_scores.title('High Scores')
        button = Button(high_scores, text='OK', padx=30, pady=3)
        button.pack(side=BOTTOM, anchor=SE, padx=5, pady=5)

    def __set_settings(self, size, mines_count, game_settings):
        self.__size = int(size.get())
        self.__mines_count = int(mines_count.get())
        game_settings.destroy()

    def __show_game_settings(self):
        game_settings = Toplevel()
        game_settings.title('Game settings')
        game_settings.geometry('300x120+500+150')
        game_settings.resizable(False, False)

        frame_1 = ttk.Frame(game_settings, padding=[5, 5])
        input_size_label = Label(frame_1, text='Field size', width=15)
        input_size_label.pack(side=LEFT, padx=10, pady=2)
        mines_count_label = Label(frame_1, text='Mines count', width=15)
        mines_count_label.pack(side=RIGHT, padx=10, pady=2)
        frame_1.pack(side=TOP, fill=X)

        frame_2 = ttk.Frame(game_settings, padding=[5, 5])
        size = Spinbox(frame_2, from_=5, to=20, justify=CENTER)
        size.pack(side=LEFT, padx=10, pady=2)
        mines_count = Spinbox(frame_2, from_=5, to=20, justify=CENTER)
        mines_count.pack(side=RIGHT, padx=10, pady=2)
        frame_2.pack(side=TOP, fill=X)

        frame_3 = ttk.Frame(game_settings, padding=[5, 5])
        button = Button(frame_3, command=(lambda: self.__set_settings(size, mines_count, game_settings)),
                        text='OK', padx=30, pady=3)
        button.pack(anchor=SE, padx=5, pady=5)
        frame_3.pack(side=TOP, fill=X)

    def f(self, button):
        button.destroy()

    def __play(self):
        width_button = 30
        size = str(width_button * self.__size)
        fields = []

        for widget in self.__field_frame.winfo_children():
            widget.destroy()

        for i in range(self.__size):
            self.__field_frame.rowconfigure(index=i, weight=1)
            self.__field_frame.columnconfigure(index=i, weight=1)

        for i in range(self.__size):
            row = []

            for j in range(self.__size):
                button = Button(self.__field_frame, padx=width_button, pady=width_button)
                button.bind('<Button-1>', lambda x=i, y=j: self.f(button))
                button.grid(row=i, column=j, sticky=NSEW)
                row.append(Field(button))

            fields.append(row)

        self.__root.geometry(size + 'x' + size + '+400+100')
        self.__root.resizable(False, False)
        self.__field_frame.pack(expand=True, fill=BOTH)
