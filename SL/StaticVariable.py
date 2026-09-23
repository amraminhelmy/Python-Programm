class Book:
    __booksBorrowed: int = 0

    def __init__(self, title, author):
        self. title = title
        self. author = author
        self. borrowed = False
        self. waitList = False

    def getTitle(self):
        return self. title

    def getAuthor(self):
        return self. author

    def getBorrowed(self):
        return self. borrowed

    def getWaitList(self):
        return self. waitList

    def setBorrowed(self, b):
        self. borrowed = b
        if (self.__borrowed):
            Book.__booksBorrowed += 1
        else:
            Book.__booksBorrowed -= 1

    def setWaitList(self, b):
        self. waitList = b

    def getNumberOfBooksBorrowed(self):
        return Book.__booksBorrowed

    def __str__(self):
        return "Title: " + self. title + ", Author: " + self. author + ", Borrowed: " + str(self. borrowed) + ", Waitlist: " + str(self. waitList)

    def getAuthor(self):
        return self. author
    
    def getBorrowed(self):
        return self.__borrowed
    
    def getWaitList(self):
        return self.__waitList
    
    def setBorrowed(self, b):
        self. borrowed = b
        if (self.__borrowed):
            Book.__booksBorrowed += 1
        else:
            Book.__booksBorrowed -= 1
    
    def setWaitList (self, b):
        self. waitList = b
    
    def getNumberOfBooksBorrowed(Book):
        return Book.__booksBorrowed
    
    def __str__(self):
        return "Title: " + self. title + ", Author: " + self. author + ", Borrowed: " + str(self. borrowed) + ", Waitlist: " + str(self. waitList)