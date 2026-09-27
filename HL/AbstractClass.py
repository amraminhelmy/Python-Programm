import abc

class abstractPerson(abc.ABC):
    @abc.abstractmethod #Unimplemented methods in the abstract class, which must be implemented by any subclass.
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_age(self):
        pass

    @abc.abstractmethod
    def introduce(self):
        pass

class Student(abstractPerson):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def get_name(self):#implementing the abstract methods in the subclass
        return self.name

    def get_age(self):
        return self.age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print(f"My student ID is {self.student_id}.")

class Teacher(abstractPerson):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print(f"I teach {self.subject}.")


print("Abstract Class Example:")
Alvise = Student("Alvise", 20, "S12345")
Alvise.introduce()

Amr = Teacher("Amr", 45, "CS")
Amr.introduce()

people = [Alvise, Amr] #this is a list of abstractPerson objects, demonstrating the concept of abstract classes and polymorphism. Each object in the list is an instance of a subclass of abstractPerson, and they can be treated as abstractPerson objects.
for person in people:
    person.introduce()