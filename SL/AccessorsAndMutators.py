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
        except ValueError as e:
            print(e)

    def get_name(self):
        return self.name

Amr = Person("Amr", 45)
Amr.set_age(30)  # Valid age
print("Age after setting to 30:", Amr.get_age())
Amr.set_age(-5)  # Invalid age
print("Age after attempting to set to -5:", Amr.get_age())
Amr.set_name("Amr123")  # Invalid name
print("Name after attempting to set to 'Amr123':", Amr.get_name())
Amr.set_name("Amr")  # Valid name
print("Name after setting to 'Amr':", Amr.get_name())
Amr.greet()
