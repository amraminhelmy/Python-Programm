from tkinter import *

window = Tk()
window.geometry("1200x800")
window.title("Federico")
window.configure(bg="lightblue")
window.config(padx=20, pady=20)
window.config(highlightbackground="red", highlightthickness=2)

photo = PhotoImage(file="2.png")
label = Label(window, image=photo)
label.pack()

counter = 0
def increment():
    global counter
    counter += 1
    print(f"Button clicked {counter} times!")

text_label = Label(window, text=f"Button clicked {counter} times!", font=("Arial", 12), bg="lightblue")
text_label.pack()

button = Button(window, text="Jessica", command=lambda: [increment(), text_label.config(text=f"Button Jessicaclicked {counter} times!")])
button.pack()

window.mainloop()