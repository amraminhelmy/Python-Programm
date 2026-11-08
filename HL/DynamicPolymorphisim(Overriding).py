class Person: #Class Superclass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is" + self.name + " and I am " + str(self.age) + " years old.")

class Student(Person): #Class Subclass
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):#Polymorphism: Overriding the introduce method of the superclass
        super().introduce()
        print("My student ID is" + str(self.student_id) + ".")

class Teacher(Person): #Class Subclass
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):#Polymorphism: Overriding the introduce method of the superclass
        super().introduce()
        print("I teach" + self.subject + ".")


Alvise = Student("Alvise", 20, "S12345")
Alvise.introduce()

Amr = Teacher("Amr", 45, "CS")
Amr.introduce()
