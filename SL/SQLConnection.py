import sqlite3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

    def set_age(self, age):
        try:
            if age < 0 or age > 120:
                raise ValueError("Age must be between 0 and 120.")
            else:
                self.age = age
        except ValueError as e:
            print(e)

    def get_age(self):
        return self.age

    def set_name(self, name):
        try:
            if not name.isalpha():
                raise ValueError("Name must contain only alphabetic characters.")
            else:
                self.name = name
                with sqlite3.connect('myfirstdb.db') as connection:
                    cursor = connection.cursor()
                    # Execute SQL commands here
                    cursor.execute('SELECT sqlite_version();')
                    print(cursor.fetchone())
                    print("Database location:", cursor.execute("PRAGMA database_list").fetchall())
                    print("Existing tables:", cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
                    cursor.execute('INSERT INTO Students (Name) VALUES (?)', (self.name,))
                    
                    cursor.close()

        except ValueError as e:
            print(e)

    def get_name(self):
        with sqlite3.connect('myfirstdb.db') as connection:
            cursor = connection.cursor()
            # Execute SQL commands here
            cursor.execute('SELECT sqlite_version();')
            print(cursor.fetchone())
            cursor.execute('SELECT Name FROM Students WHERE Name = ?', (self.name,))
            return cursor.fetchone()[0]

Amr=Person("Amr", 20)
Amr.set_name("AmrHelmyALivse")
print(Amr.get_name())

