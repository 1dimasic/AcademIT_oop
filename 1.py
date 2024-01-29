from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
image = Image.open('mine.gif')
image = image.resize((20, 20))
bomb_logo = ImageTk.PhotoImage(image)
b = Label(root, image=bomb_logo)
b.grid()
root.mainloop()
