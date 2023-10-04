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
        with open('data/high scores.dat', 'r') as file:
            high_scores = Toplevel()
            high_scores.geometry('300x300+500+150')
            high_scores.title('High Scores')
            high_scores_table = file.readline()
            label = Label(high_scores, text=high_scores_table)
            button = Button(high_scores, text='OK', command=high_scores.quit, padx=30, pady=3)
            button.pack(side=BOTTOM, anchor=SE, padx=5, pady=5)
            label.pack(expand=YES)

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

        for x in range(size_x):
            for y in range(size_y):
                button = Button(self.__fields_frame, text=field[x][y], width=2)
                button.grid(row=x, column=y, sticky=NSEW)
                button.bind('<Button-1>', lambda event, i=x, j=y: self.__controller.pushed_left_click(i, j))
                button.bind('<Button-3>', lambda event, i=x, j=y: self.__controller.pushed_right_click(i, j))

        height = str(24 * size_y)
        width = str(26 * size_x)
        self.__root.geometry(height + 'x' + width)
        self.__fields_frame.pack(expand=True, fill=BOTH)

    def show_all_mines_and_game_over(self, minefields):
        # TODO Картинка бомбы
        # bomb_logo = PhotoImage(file='')

        for x, y in minefields:
            label = Label(self.__fields_frame, text='b', width=2)
            label.grid(row=x, column=y, sticky=NSEW)

        for widget in self.__fields_frame.winfo_children():
            if isinstance(widget, Button):
                widget.config(state='disabled')
                widget.unbind('<Button-1>')
                widget.unbind('<Button-3>')

    def hide_flag(self, data, x, y):
        current_button = self.__fields_frame.grid_slaves(row=x, column=y)[0]
        current_button.config(text=data)
        current_button.bind('<Button-3>', lambda event, i=x, j=y: self.__controller.pushed_right_click(i, j))

    def show_flag(self, x, y):
        # TODO Картинка флажка
        # bomb_logo = PhotoImage(file='')
        current_button = self.__fields_frame.grid_slaves(row=x, column=y)[0]
        current_button.config(text='f')
        current_button.unbind('<Button-3>')

    def show_winning_message(self, game_time):
        for widget in self.__fields_frame.winfo_children():
            if isinstance(widget, Button) and not isinstance(widget['text'], str):
                widget.config(state='disabled')
            else:
                widget.unbind('<Button-1>')
                widget.unbind('<Button-3>')

        win = Toplevel()
        message = f'Congratulations!\nYour win!\nYour time: {game_time:.2f}'
        win.geometry('300x300+500+150')
        win.title('Your win!')
        label_1 = Label(win, text=message)
        label_2 = Label(win, text='Enter your name')
        player_name = Entry(win)

        button = Button(win, text='OK', command=lambda: self.__controller.add_1(player_name.get(), game_time),
                        padx=30, pady=3)
        button.pack(side=BOTTOM, anchor=SE, padx=5, pady=5)
        label_1.pack(side=TOP)
        label_2.pack()
        player_name.pack()

    def show_field(self, x, y, data):
        label = Label(self.__fields_frame, text=data, width=2)
        label.grid(row=x, column=y, sticky=NSEW)
