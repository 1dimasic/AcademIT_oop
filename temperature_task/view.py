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

    def set_controller(self, controller):
        self.__controller = controller

    def start(self):
        self.__root = Tk()
        self.__root.title('Temperature converter')
        self.__root.geometry('350x600+500+50')

        frame_1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        frame_2 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])

        input_label = ttk.Label(frame_1, text='Input temperature in scale:')
        input_label.pack(fill=X, pady=5)

        self.__input_entry = ttk.Entry(frame_1)
        self.__input_entry.pack(fill=X, pady=5)

        self.__input_scale = StringVar()
        scales = list(Scale)

        for scale in scales:
            input_scale = ttk.Radiobutton(frame_1, text=scale, value=scale, variable=self.__input_scale)
            input_scale.pack(side=LEFT)

        output_label = ttk.Label(frame_2, text='Convert temperature to scale:')
        output_label.pack(fill=X, pady=5)

        self.__output_scale = {scale: 0 for scale in scales}

        for scale in scales:
            self.__output_scale[scale] = IntVar()
            output_scale = ttk.Checkbutton(frame_2, text=scale, variable=self.__output_scale[scale])
            output_scale.pack(side=LEFT, pady=5)

        frame_1.pack(fill=X, padx=5, pady=5)
        frame_2.pack(fill=X, padx=5, pady=5)

        convert_button = ttk.Button(text='Convert', command=self.__convert_temperature)
        convert_button.pack(fill=X, padx=5, pady=5)

        self.__root.mainloop()

    def show(self, output_temperature):
        frame_4 = ttk.Frame(self.__root)
        result_label = ttk.Label(frame_4, text=output_temperature)
        result_label.pack(fill=BOTH)
        frame_4.pack(fill=X, padx=5, pady=5)

    def __convert_temperature(self):
        input_temperature = 0

        try:
            input_temperature = float(self.__input_entry.get())
        except ValueError:
            self.show(f'Incorrect type {type(self.__input_entry.get())}, need int or float')

        input_scale = self.__input_scale.get()

        if not input_scale:
            self.show(f'Select input scale')

        output_scale = []

        for key in self.__output_scale.keys():
            if self.__output_scale[key].get() == 1:
                output_scale.append(key)

        if not output_scale:
            self.show(f'Select output scale')

        self.__controller.convert_temperature(input_temperature, input_scale, output_scale)
