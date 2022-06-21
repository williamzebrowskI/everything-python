


class Book:
    #def __init__(self, title):
     #   self.title = title
    BOOK_TYPES = ('Hardcover', 'Paperback', 'Ebook')

    def setTitle(self, newtitle):
        self.title = newtitle

    #create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

print('Book types: ', Book.getbooktypes())
    
class Newspaper:
    def __init__(self, name):
        self.name = name

#Create some instances for the classes

#b1 = Book('The Cather in the rye')
#b2 = Book('The grapes of Wrath')
n1 = Newspaper('The Washington Post')
n2 = Newspaper('The New York Times')
b3 = Book('Title 1', 'Hardcover')
b4 = Book('Title 2', 'comic')
#use type() to inspect the object type
#print(type(b1))
#print(type(n1))

#compare two types together
#print(type(b1) == type(b2))
#print(type(b1) == type(n2))

#use isinstance to compare a specific instance to a known type
#print(isinstance(b1, Book))
#print(isinstance(n1, Newspaper))
#print(isinstance(n2, Book))
#print(isinstance(n2, object))

