from tkinter import *
import tkinter
import GUI1

class window2(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("My Second Window")
        label2 = Label(self, text="This is the second window", font=("Arial", 16))
        label2.pack(pady=20)
        open_window1_button = Button(self, text="Open Window 1", command=self.open_window1)
        open_window1_button.pack(pady=10)

    def open_window1(self):
        self.destroy()
        GUI1.window1().mainloop()
