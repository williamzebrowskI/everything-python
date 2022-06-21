# f string = can place variables inside a string.
day = 3

month = 'October'
temp = -15
day_name = 'Tuesday'

print(f"Today is {day_name} {month} {day} and its {temp} degrees outside")


#String Objects

print('Hello World!'.upper())
print('Hello World!'.swapcase())
print('Hello World! {}'.format(42*7))

s = 'Hello World! {}'
print(s.format(42 * 7))

#subclass
class MyString(str):
    def __str__(self):
        return self[::-1]

b = MyString('Hello, World.')
print(b)


#Common String Objects  A string is immuniteable, it cant be changed.
#methods
print('Hello World!'.title())
print('Hello World!'.casefold())
print('Hello World!'.lower())

s1 = 'Hello World!'
s2 = 'This is another string'

#concatinated string:
s3 = 'This is a string' ' This is a string'

print(s1 + ' ' + s2)
print(s3)


#Format Strings
x = 32
print('The number is {}'.format(x))
print(f'The number is {x}')



#Splitting and Joining

s = 'This is my favorite sentence in the world.'

l = s.split()
s2 = ':'.join(l)

print(s.split())
print(s2)



x = 'www.google.com'
y = {}

for i in x:    #
    if i in y:
        y[i] +=1
    else:
        y[i] = 1
print(y)


hello ='hello there'
print(hello[::-1][0])

word = 'stringify'
even_letters = [c for i, c in enumerate(word) if i % 2 == 0]
odd_letters = [c for i, c in enumerate(word) if i % 2 == 1]
print(even_letters)
print(odd_letters)