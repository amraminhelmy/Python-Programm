from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("First GUI Application")
window.configure(bg="lightblue")
window.config(padx=20, pady=20)
window.config(highlightbackground="red", highlightthickness=2)

photo = PhotoImage(file="2.png")
label = Label(window, image=photo)
label.pack()

window.mainloop()