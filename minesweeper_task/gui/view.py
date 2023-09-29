import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk


class View:
    def __init__(self):
        self.__root = Tk()
        self.__controller = None
        self.__fields_frame = None

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__root.geometry('300x300+500+200')
        self.__root.title('Minesweeper')
        self.__add_menu()
        self.__fields_frame = ttk.Frame()
        self.__fields_frame.pack(expand=YES)
        self.__root.mainloop()

    def __add_menu(self):
        top = Menu(self.__root, tearoff=0)
        self.__root.config(menu=top)
        top.add_command(label='New game', command=self.__controller.prepare)
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

    def __set_settings(self, x, y, mines_count, game_settings):
        size_x = int(x.get())
        size_y = int(y.get())
        mines_count = int(mines_count.get())
        self.__controller.prepare(size_x, size_y, mines_count)
        game_settings.destroy()

    def __show_game_settings(self):
        game_settings = Toplevel()
        game_settings.title('Game settings')
        game_settings.geometry('250x120+500+150')
        game_settings.resizable(False, False)

        frame_1 = ttk.Frame(game_settings, padding=[5, 5])
        input_size_label = Label(frame_1, text='Field size', width=15)
        input_size_label.pack(side=LEFT)
        mines_count_label = Label(frame_1, text='Mines count', width=15)
        mines_count_label.pack(side=RIGHT)
        frame_1.pack(side=TOP, fill=X)

        frame_4 = ttk.Frame(game_settings, padding=[5, 5])
        button = Button(frame_4, command=(lambda: self.__set_settings(size_x, size_y, mines_count, game_settings)),
                        text='OK', padx=30, pady=5)
        button.pack(fill=X, padx=15, pady=2)
        frame_4.pack(side=BOTTOM, fill=X)

        frame_2 = ttk.Frame(game_settings)
        size_x = Spinbox(frame_2, from_=9, to=20, justify=CENTER, width=5)
        size_x.pack(side=LEFT, padx=2)
        size_y = Spinbox(frame_2, from_=9, to=20, justify=CENTER, width=5)
        size_y.pack(side=RIGHT, padx=2)
        frame_2.pack(side=LEFT, fill=X, padx=20, pady=2)

        frame_3 = ttk.Frame(game_settings)
        mines_count = Spinbox(frame_3, from_=10, to=50, justify=CENTER, width=15)
        mines_count.pack(side=RIGHT)
        frame_3.pack(side=RIGHT, fill=X, padx=20, pady=2)

    def add_widgets_on_game_field(self, field, size_x, size_y):
        for widget in self.__fields_frame.winfo_children():
            widget.destroy()

        for i in range(size_x):
            for j in range(size_y):
                button = Button(self.__fields_frame, command=(lambda x=i, y=j: self.__controller.play(x, y)), width=2)
                button.grid(row=i, column=j, sticky=NSEW)

        height = str(24 * size_y)
        width = str(26 * size_x)
        self.__root.geometry(height + 'x' + width)
        self.__fields_frame.pack(expand=True, fill=BOTH)
