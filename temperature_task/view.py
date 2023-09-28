from tkinter import *
from tkinter import ttk
from temperature_task.scale import Scale


class View:
    def __init__(self):
        self.__root = None
        self.__controller = None
        self.__input_entry = None
        self.__input_scale = None
        self.__output_scale = None
        self.__text = None

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__root = Tk()
        self.__root.title('Temperature converter')
        self.__root.geometry('350x600+500+50')
        self.__root.resizable(False, False)

        frame_1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        frame_2 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])

        input_label = ttk.Label(frame_1, text='Input temperature in scale:', font=('Arial', '14'), foreground='blue')
        input_label.pack(fill=X, pady=5)

        self.__input_entry = ttk.Entry(frame_1)
        self.__input_entry.pack(fill=X, pady=5)

        self.__input_scale = StringVar()

        for scale in list(Scale):
            input_scale = ttk.Radiobutton(frame_1, text=scale, value=scale, variable=self.__input_scale)
            input_scale.pack(side=LEFT, fill=X)

        output_label = ttk.Label(frame_2, text='Convert temperature to scale:', font=('Arial', '14'), foreground='blue')
        output_label.pack(fill=X, pady=5)

        self.__output_scale = {scale: 0 for scale in list(Scale)}

        for scale in list(Scale):
            self.__output_scale[scale] = IntVar()
            output_scale = ttk.Checkbutton(frame_2, text=scale, variable=self.__output_scale[scale])
            output_scale.pack(side=LEFT, pady=5)

        frame_1.pack(fill=X, padx=5, pady=5)
        frame_2.pack(fill=X, padx=5, pady=5)

        convert_button = Button(text='Convert', command=self.__convert_temperature,
                                font=('Arial', '10', 'bold'), fg='red')
        convert_button.pack(fill=X, padx=5, pady=5)

        frame_3 = ttk.Frame(self.__root)
        clear_button = Button(frame_3, text='Clear', command=self.clear, font=('Arial', '10', 'bold'), fg='black')
        clear_button.pack(side=BOTTOM, anchor=SE)
        scrollbar = ttk.Scrollbar(frame_3)
        self.__text = Text(frame_3, font=('Arial', '10'))
        scrollbar.config(command=self.__text.yview)
        self.__text.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.__text.pack(side=LEFT, expand=YES, fill=BOTH)
        frame_3.pack(fill=X, padx=5, pady=5)
        self.__root.mainloop()

    def clear(self):
        self.__text.delete('1.0', END)

    def show(self, output_temperature):
        output_text = ''

        if isinstance(output_temperature, dict):
            for key in self.__output_scale.keys():
                if self.__output_scale[key].get() == 1:
                    output_text += f'Temperature in {key} scale = {round(output_temperature[key], 2)}\n'

            if output_text:
                output_text += '\n'

        if isinstance(output_temperature, str):
            output_text += output_temperature

        self.__text.insert('1.0', output_text)

    def __convert_temperature(self):
        input_temperature = 0

        try:
            input_temperature = float(self.__input_entry.get())
        except ValueError:
            self.show('Input value type must be a number\n')

        input_scale = self.__input_scale.get()

        if not input_scale:
            self.show('Select input scale\n')

        self.__controller.convert_temperature(input_temperature, input_scale)
