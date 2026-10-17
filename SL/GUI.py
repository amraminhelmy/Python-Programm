from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("1200x800")
window.title("Bunny")
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

button = Button(window, text="Bunny", command=lambda: [increment(), text_label.config(text=f"Button Bunny clicked {counter} times!")])
button.pack()

def submit():
    user_input = entry.get()
    print(f"User input: {user_input}")


submit_button = Button(window, text="Submit", command=submit)
entry = Entry(window)
entry.pack()
submit_button.pack()

def warning():
    messagebox.showwarning("Warning", "This is a warning message!")

warning_button = Button(window, text="Show Warning", command=warning)
warning_button.pack()

window.mainloop()