

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

class Sentences:
    coat = ['furry', 'fluffy', 'dirty']
    animal = ['dog', 'cat', 'bird']
    action = ['play', 'be lazy', 'eat']

    def fur(self):
        print(self.coat)

    def type(self):
        print(self.animal)
    
    def to_do(self):
        print(self.action)

def main():
    words = Sentences()
    words.fur()
    words.type()
    words.to_do()
    print(words.to_do)

    


def main():
    donald = Duck()
    donald.quack()
    #or
    print(donald.sound)
    donald.move()

if __name__ == '__main__': main()



# __init__ is a initializer.  (self) makes it an object a method


# __str__ is a string representation of the option.  allows us to print the object w/o the function: print(a1)


#Create a class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attr'

#Create instance methods
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount      #the _ in front of discount hints that this attr is only internal to the class and shouldnt be access outside the class.


#ceate instances of the class
b1 = Book("Brave new world", "Harry tell", 1442, 39.00)
b2 = Book('War and Peace', "Billy Boy", 54, 49.99)


#print the class and property
#print(b1.getprice())
print(b1.getprice())
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())
print(b2._Book__secret)
#print(b1)
#print(b1.title)
#print(b2.title)


