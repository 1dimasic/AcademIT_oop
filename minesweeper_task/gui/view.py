import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from PIL import Image, ImageTk


class View:
    def __init__(self):
        self.__root = Tk()
        self.__controller = None
        self.__logos = {}

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__logos['flag'] = ImageTk.PhotoImage(Image.open('data/flag.png').resize((15, 15)))
        self.__logos['bomb'] = ImageTk.PhotoImage(Image.open('data/bomb.jpg').resize((18, 18)))
        self.__logos['main_logo'] = ImageTk.PhotoImage(Image.open('data/main_logo.png'))
        self.__logos['1'] = ImageTk.PhotoImage(Image.open('data/numbers/1.png').resize((18, 18)))
        self.__logos['2'] = ImageTk.PhotoImage(Image.open('data/numbers/2.png').resize((18, 18)))
        self.__logos['3'] = ImageTk.PhotoImage(Image.open('data/numbers/3.png').resize((18, 18)))
        self.__logos['4'] = ImageTk.PhotoImage(Image.open('data/numbers/4.png').resize((18, 18)))
        self.__logos['5'] = ImageTk.PhotoImage(Image.open('data/numbers/5.png').resize((18, 18)))
        self.__logos['6'] = ImageTk.PhotoImage(Image.open('data/numbers/6.png').resize((18, 18)))
        self.__logos['7'] = ImageTk.PhotoImage(Image.open('data/numbers/7.png').resize((18, 18)))
        self.__logos['8'] = ImageTk.PhotoImage(Image.open('data/numbers/8.png').resize((18, 18)))

        self.__controller.start()
        self.__root.title('Minesweeper')
        self.__add_menu()
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
        win = Toplevel()
        win.title('Таблица рекордов')
        win.geometry('275x305+500+150')
        win.config(padx=10, pady=10)
        win.resizable(False, False)

        high_scores = self.__controller.get_high_scores()

        for i in range(11):
            win.rowconfigure(index=i, weight=1)

        for i in range(2):
            win.columnconfigure(index=i, weight=1)

        for i in range(len(high_scores)):
            Label(win, text=high_scores[i][0], font=('Arial', 12), justify=LEFT).grid(row=i, column=0)
            Label(win, text=high_scores[i][1], font=('Arial', 12), justify=LEFT).grid(row=i, column=1)

        Button(win, text='OK', width=15, command=win.destroy).grid(row=10, column=1, sticky=E)

    def __set_settings(self, rows_count, columns_count, mines_count, window):
        is_game_options_correct = self.__controller.start(rows_count.get(), columns_count.get(), mines_count.get())
        if not is_game_options_correct[0]:
            Label(window, text=is_game_options_correct[1], foreground="red").grid(row=2, column=0)
        else:
            window.destroy()

    def __show_game_settings(self):
        game_settings = Toplevel()
        game_settings.title('Game settings')
        game_settings.geometry('345x125+500+150')
        game_settings.resizable(False, False)
        font = ('Arial', 10,)

        for i in range(3):
            game_settings.rowconfigure(index=i, weight=1)

        game_settings.columnconfigure(index=0, weight=7)
        game_settings.columnconfigure(index=1, weight=3)
        game_settings.columnconfigure(index=2, weight=1)
        game_settings.columnconfigure(index=3, weight=3)

        game_settings.config(padx=10, pady=10)

        Label(game_settings, text='Размер поля', font=font, justify=LEFT).grid(row=0, column=0)
        rows_count = Entry(game_settings, width=3, font=font, justify=CENTER)
        rows_count.grid(row=0, column=1, sticky=EW)
        Label(game_settings, text='x', font=font).grid(row=0, column=2)
        columns_count = Entry(game_settings, width=3, font=font, justify=CENTER)
        columns_count.grid(row=0, column=3, sticky=EW)

        Label(game_settings, text='Количество мин', font=font, justify=LEFT).grid(row=1, column=0)
        mines_count = Entry(game_settings, width=10, font=font, justify=CENTER)
        mines_count.grid(row=1, column=1, columnspan=3, sticky=EW)

        button = Button(game_settings, text='OK', width=10)
        button.bind('<Button-1>',
                    lambda event: self.__set_settings(rows_count, columns_count, mines_count, game_settings))
        button.grid(row=2, column=1, columnspan=3, sticky=E)

    def init_game_field(self, width, height):
        for x in range(width):
            for y in range(height):
                button = ttk.Button(self.__root, width=3)
                button.grid(row=x, column=y, sticky=NSEW)
                button.bind('<Button-1>', lambda event, i=x, j=y: self.__controller.click_left(i, j))
                button.bind('<Button-3>', lambda event, i=x, j=y: self.__controller.click_right(i, j))

        self.__root.resizable(False, False)

    def show_mines_and_game_over(self, fields):
        for i in range(len(fields)):
            for j in range(len(fields[i])):
                if fields[i][j].data == -1:
                    label = Label(self.__root, image=self.__logos['bomb'])
                    label.grid(row=i, column=j, sticky=NSEW)
                    continue

                if 1 <= fields[i][j].data <= 8:
                    label = Label(self.__root, image=self.__logos[str(fields[i][j].data)])
                    label.grid(row=i, column=j, sticky=NSEW)
                    continue

                label = Label(self.__root, image='')
                label.grid(row=i, column=j, sticky=NSEW)

    def hide_flag(self, x, y):
        current_button = self.__root.grid_slaves(row=x, column=y)[0]
        current_button['image'] = ''
        current_button.bind('<Button-1>', lambda event: self.__controller.click_left(x, y))

    def show_flag(self, x, y):
        current_button = self.__root.grid_slaves(row=x, column=y)[0]
        current_button['image'] = self.__logos['flag']
        current_button.unbind('<Button-1>')

    def __close_winning_message(self, name, time, window):
        if len(name) != 0:
            self.__controller.add_player(name, time)
            window.destroy()

    def show_winning_message(self, time):
        for widget in self.__root.winfo_children():
            widget.unbind('<Button-1>')
            widget.unbind('<Button-2>')
            widget.unbind('<Button-3>')

        win = Toplevel()
        win.geometry('230x155+500+150')
        win.resizable(False, False)
        win.title('ПОБЕДА!')

        for i in range(5):
            win.rowconfigure(index=i, weight=1)

        win.columnconfigure(index=0, weight=1)

        Label(win, text='Вы победили!', foreground='red', justify=CENTER, font=('Arial', 14, 'bold')).grid(row=0,
                                                                                                           column=0)
        Label(win, text=f'Ваше время: {time:.1f}', justify=CENTER, font=('Arial', 12, 'bold')).grid(row=1,
                                                                                                    column=0)
        Label(win, text='Введите Ваше имя', font=('Arial', 12)).grid(row=2, column=0)
        name = Entry(win, width=15, font=('Arial', 12))
        name.grid(row=3, column=0)

        button = Button(win, text='OK', padx=30, pady=3)
        button.bind('<Button-1>',
                    lambda event: self.__close_winning_message(name.get(), time, win))
        button.grid(row=4, column=0)

    def open_field(self, fields):
        for x, y in fields.keys():
            image = self.__logos[str(fields[(x, y)])] if fields[(x, y)] != 0 else ''
            label = Label(self.__root, width=2, image=image)
            label.grid(row=x, column=y, sticky=NSEW)
