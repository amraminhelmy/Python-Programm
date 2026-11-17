import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter
import GUI2

class window1(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x1200")
        self.title("Bunny")
        self.configure(bg="blue")
        self.config(padx=20, pady=20)
        self.config(highlightbackground="red", highlightthickness=2)
        self.photo = PhotoImage(file="2.png")
        self.label = Label(self, image=self.photo)
        self.label.pack(pady=10)
        self.text_label = Label(self, text=f"Button clicked {self.counter} times!", font=("Arial", 12), bg="blue")
        self.text_label.pack(pady=10)
        button = Button(self, text="Bunny", command=lambda: [self.increment(), self.text_label.config(text=f"Button Bunny clicked {self.counter} times!")])
        button.pack(pady=10)
        submit_button = Button(self, text="Submit", command=lambda: self.find(self.entry), bg="green", fg="white", font=("Arial", 12, "bold"))
        submit_button.pack(pady=10)
        entry = Entry(self, width=30, font=("Arial", 12))
        entry.pack(pady=10)  
        warning_button = Button(self, text="Show Warning", command=self.warning)
        warning_button.pack(pady=10)
        yes_no_button = Button(self, text="Yes/No", command=self.yes_no)
        yes_no_button.pack(pady=10)
        open_window2_button = Button(self, text="Open Window 2", command=self.open_window2)
        open_window2_button.pack(pady=10)


    counter = 0
    def increment(self):
        self.counter += 1
        print(f"Button clicked {self.counter} times!")

    def submit(self, entry):
        user_input = entry.get()
        print(f"User input: {user_input}")

    def find(self, entry):
        Name = entry.get()
        with sqlite3.connect('myfirstdb.db') as connection:
            cursor = connection.cursor()
            # Execute SQL commands here
            cursor.execute('SELECT sqlite_version();')
            print(cursor.fetchone())
            cursor.execute('SELECT Name FROM Students WHERE Name = ?', (Name,))
            result = cursor.fetchone()
        if result is not None:
            
            print("found")
        else:
            print("Not Found", "No matching record found.")
        return None

    def warning(self):
        messagebox.showwarning("Warning", "This is a warning message!")

    def yes_no(self):
        response = messagebox.askyesno("Question", "Do you want to proceed?")
        if response:
            print("User chose Yes.")
        else:
            print("User chose No.")

    def open_window2(self):
            self.destroy()
            GUI2.window2().mainloop()

    
