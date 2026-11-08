class Book:
    def __init__(self, title, subject):
        self.__title = title
        self.__subject = subject
        self.__units = []

    def getTitle(self):
        return self.__title

    def getSubject(self):
        return self.__subject

    def getUnit(self, unit):
        return self.__units[unit]

    def addUnit(self, unit):
        self.__units.append(unit)

    def removeUnit(self, unit):
        self.__units.remove(unit)

    def getUnits(self):
        for unit in self.__units:
            print(unit)
    
    def __str__(self):
        return "Title: " + self.__title + ", Subject: " + self.__subject + ", Units: " + str(self.__units)

class Unit:
    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def getTitle(self):
        return self.__title

    def getContent(self):
        return self.__content

    def __str__(self):
        return "Title: " + self.__title + ", Content: " + self.__content

BookCS = Book("Computer Science", "CS")
BookCS.addUnit(Unit("Unit 1", "Computer fundamentals"))
BookCS.addUnit(Unit("Unit 2", "Networks"))
BookCS.addUnit(Unit("Unit 3", "Databases"))

print(BookCS.getUnit(0))  # Output: Title: Unit 1, Content: Computer fundamentals
print(BookCS.getUnit(1).getTitle())  # Output: Unit 2
print(BookCS.getUnit(2).getContent())  # Output: Databases

print(BookCS.getUnits())# Output: Title: Unit 1, Content: Computer fundamentals. Title: Unit 2, Content: Networks. Title: Unit 3, Content: Databases
