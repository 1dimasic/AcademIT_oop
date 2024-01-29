import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from operator import itemgetter
from PIL import ImageTk, Image


class View:
    def __init__(self):
        self.__root = Tk()
        self.__controller = None
        self.__game_field = None

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__root.geometry('300x300+500+200')
        self.__root.title('Minesweeper')
        self.__add_menu()
        self.__game_field = ttk.Frame()
        self.__game_field.pack(expand=YES)
        self.__root.mainloop()

    def __add_menu(self):
        main_menu = Menu(self.__root, tearoff=0)
        self.__root.config(menu=main_menu)
        game_menu = Menu(main_menu, tearoff=0)
        game_menu.add_command(label='New game', command=self.__controller.start)
        game_menu.add_command(label='Settings', command=self.__show_game_settings)
        main_menu.add_cascade(label='Game', menu=game_menu)
        main_menu.add_command(label='High scores', command=self.__show_high_scores)
        main_menu.add_command(label='About', command=self.__show_about)
        main_menu.add_command(label='Exit', command=sys.exit)

    @staticmethod
    def __show_about():
        with open('data/about.dat', 'r') as file:
            showinfo(title='About', message=file.read(), default='ok')

    def __show_high_scores(self):
        high_scores = Toplevel()
        high_scores.geometry('250x300+500+150')
        high_scores.resizable(False, False)
        high_scores.title('High Scores')
        high_scores_info = sorted(self.__controller.load_high_scores(), key=itemgetter(1))[:10]
        names = ''
        time = ''

        for i in range(len(high_scores_info)):
            names += str(high_scores_info[i][0]) + '\n'
            time += str(high_scores_info[i][1]) + '\n'

        button = Button(high_scores, text='OK', command=high_scores.destroy, padx=30, pady=3)
        button.pack(side=BOTTOM, anchor=SE, padx=5, pady=5)
        label_names = Label(high_scores, text=names, font=('Arial', 12, 'bold'), foreground='green', anchor=N)
        label_time = Label(high_scores, text=time, font=('Arial', 12, 'bold'), foreground='red', anchor=N)
        label_names.pack(side=LEFT, fill=Y)
        label_time.pack(side=RIGHT, fill=Y)

    def __set_settings(self, x, y, mines_count, window):
        size_x = int(x.get())
        size_y = int(y.get())
        mines_count = int(mines_count.get())
        self.__controller.start(size_x, size_y, mines_count)
        window.destroy()

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
        button = Button(frame_4, text='OK', padx=30, pady=5)
        button.bind('<Button-1>', lambda event: self.__set_settings(size_x, size_y, mines_count, game_settings))
        button.pack(fill=X, padx=15, pady=2)
        frame_4.pack(side=BOTTOM, fill=X)

        frame_2 = ttk.Frame(game_settings)
        size_x = Spinbox(frame_2, from_=9, to=20, justify=CENTER, width=5, state='readonly')
        size_x.pack(side=LEFT, padx=2)
        size_y = Spinbox(frame_2, from_=9, to=20, justify=CENTER, width=5, state='readonly')
        size_y.pack(side=RIGHT, padx=2)
        frame_2.pack(side=LEFT, fill=X, padx=20, pady=2)

        frame_3 = ttk.Frame(game_settings)
        mines_count = Spinbox(frame_3, from_=10, to=40, justify=CENTER, width=15, state='readonly')
        mines_count.pack(side=RIGHT)
        frame_3.pack(side=RIGHT, fill=X, padx=20, pady=2)

    def add_fields(self, width, height, a):
        for widget in self.__game_field.winfo_children():
            widget.destroy()

        for x in range(width):
            for y in range(height):
                button = Button(self.__game_field, width=2, text=a[x][y])
                button.grid(row=x, column=y, sticky=NSEW)
                button.bind('<Button-1>', lambda event, i=x, j=y: self.__controller.pushed_left_click(i, j))
                button.bind('<Button-2>', lambda event, i=x, j=y: self.__controller.pushed_center_click(i, j))
                button.bind('<ButtonRelease-2>', lambda event, i=x, j=y: self.__controller.unpushed_center_click(i, j))
                button.bind('<Button-3>', lambda event, i=x, j=y: self.__controller.pushed_right_click(i, j))

        self.__root.geometry(str(24 * height) + 'x' + str(26 * width))
        self.__game_field.pack(expand=True, fill=BOTH)
        self.__root.resizable(False, False)

    def show_all_mines_and_game_over(self, minefields):
        # TODO Картинка бомбы
        image = Image.open('data/mine.gif')
        image = image.resize((20, 20))
        bomb_logo = ImageTk.PhotoImage(image)

        for x, y in minefields:
            label = Label(self.__game_field, image=bomb_logo)
            label.grid(row=x, column=y, sticky=NSEW)

        for widget in self.__game_field.winfo_children():
            if isinstance(widget, Button):
                widget.config(state='disabled', text='')
                widget.unbind('<Button-1>')
                widget.unbind('<Button-3>')

    def put_away_flag(self, x, y):
        current_button = self.__game_field.grid_slaves(row=x, column=y)[0]
        current_button.config(image='')
        current_button.bind('<Button-1>', lambda event, i=x, j=y: self.__controller.pushed_left_click(i, j))

    def put_flag(self, x, y):
        # TODO Картинка флажка
        image = Image.open('data/flag.gif')
        image = image.resize((20, 20))
        flag_logo = ImageTk.PhotoImage(image)

        current_button = self.__game_field.grid_slaves(row=x, column=y)[0]
        current_button.config(image=flag_logo)
        current_button.unbind('<Button-1>')

    def __set_new_name_and_time(self, name, time, window):
        if len(name) != 0:
            self.__controller.add_to_high_scores([name, time])
            window.destroy()

    def show_winning_message(self, game_time):
        for widget in self.__game_field.winfo_children():
            if isinstance(widget, Button):
                if not isinstance(widget['text'], str):
                    widget.config(state='disabled')
                else:
                    widget.unbind('<Button-1>')
                    widget.unbind('<Button-3>')

        win = Toplevel()
        message = f'    Your win!\nYour time: {game_time:.2f}'
        win.geometry('300x200+500+150')
        win.resizable(False, False)
        win.title('Your win!')
        label_1 = Label(win, text=message, font=('Arial', 14, 'bold'), foreground='red', justify=LEFT)
        label_2 = Label(win, text='Enter your name', font=('Arial', 12, 'bold'))
        player_name = Entry(win, width=15, font=('Arial', 14))

        button = Button(win, text='OK', padx=30, pady=3)
        button.bind('<Button-1>',
                    lambda event: self.__set_new_name_and_time(player_name.get(), round(game_time, 1), win))
        button.pack(side=BOTTOM, anchor=SE, padx=5, pady=5)
        label_1.pack(side=TOP)
        label_2.pack()
        player_name.pack()

    def open_field(self, *args):
        if len(args) == 3:
            x = args[0]
            y = args[1]
            data = args[2]
            label = Label(self.__game_field, text=data, width=2)
            label.grid(row=x, column=y, sticky=NSEW)

        if len(args) == 1:
            open_field = args[0].copy()

            for x, y in open_field:
                label = Label(self.__game_field, text=open_field[(x, y)], width=2)
                label.grid(row=x, column=y, sticky=NSEW)

    def f(self, l):
        for x, y in l:
            current_widget = self.__game_field.grid_slaves(row=x, column=y)[0]

            if isinstance(current_widget, Button):
