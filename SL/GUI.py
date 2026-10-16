from tkinter import *

window = Tk()
window.geometry("1200x800")
window.title("Simple GUI")
window.configure(bg="lightblue")
window.config(padx=20, pady=20)
window.config(highlightbackground="red", highlightthickness=2)

photo = PhotoImage(file="2.png")  # Replace with your image path
label = Label(window, image=photo)
label.pack(pady=10)

count = 0
button = Button(window, text="Click Me", command=lambda: increment_count())
button.pack(pady=10)

def increment_count():
    global count
    count += 1
    print(f"Button clicked {count} times")

window.mainloop()