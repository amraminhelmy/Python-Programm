import GUI1
import GUI2
from tkinter import *

homwindow = Tk()
homwindow.geometry("1200x800")
homwindow.title("My Home Window")
label = Label(homwindow, text="This is the home window", font=("Arial", 16))
label.pack(pady=20)
Open_Window1 = Button(homwindow, text="Open Window 1", command=lambda: [homwindow.destroy(), GUI1.window1().mainloop()])
Open_Window1.pack(pady=10)
Open_Window2 = Button(homwindow, text="Open Window 2", command=lambda: [homwindow.destroy(), GUI2.window2().mainloop()])
Open_Window2.pack(pady=10)
homwindow.mainloop()