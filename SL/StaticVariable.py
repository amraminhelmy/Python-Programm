class Book:
    __booksBorrowed: int = 0

    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__borrowed = False
        self.__waitList = False

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getBorrowed(self):
        return self.__borrowed

    def getWaitList(self):
        return self.__waitList

    def setBorrowed(self, b):
        self.__borrowed = b
        if (self.__borrowed):
            Book.__booksBorrowed += 1
        else:
            Book.__booksBorrowed -= 1

    def setWaitList(self, b):
            self.__waitList = b

    def getNumberOfBooksBorrowed(Book): #notice the Static method uses the class name as a parameter
        return Book.__booksBorrowed #notice the refrence to the class variable, not the instance variable

    def __str__(self):
        return "Title: " + self.__title + ", Author: " + self.__author + ", Borrowed: " + str(self.__borrowed) + ", Waitlist: " + str(self.__waitList)

one = Book("Community and Support", "D Larkin")
two = Book("Where is Archibald", "C Rington")
three = Book("Horticulture for the Balcony", "A Abed")
one.setBorrowed(True)
two.setBorrowed(True)
two.setWaitList(True)
print(one.__str__())
print(two.__str__())
print("The number of books borrowed is: ", Book.getNumberOfBooksBorrowed(Book))