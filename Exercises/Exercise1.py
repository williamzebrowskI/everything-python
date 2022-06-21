# Given two integer numbers return their product only 
# if the product is equal to or lower than 1000, else return their sum.

def multi_or_sum(a, b):
    if a * b <= 1000:
        print(f'The result is {a * b}')
    elif a + b <= 1000:
        print(f'The result is {a + b}')



# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration
# print the sum of the current and previous number.

def current_plus_prev():
    for i in range(1, 10):
        print(f'Current Number {i} Previous Number {i - 1} Sum {i + (i - 1)}')



#Exercise 3: Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.
#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# accept input string from a user
#word = input('Enter word ')
#print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars

#x = list(word)
def Exercise3():
    for i in x[0::2]:
        print(i)


# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero 
# up to n and return a new string.
# For example:
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.

#n = len(word)

def remove_chars(word, x):
    print(word[x:])

#remove_chars('BananananaBan', 4)


#Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

x = [10, 20, 30, 40, 10]
y = [75, 65, 35, 75, 30]

def Exercise5(n):
    if n[0] == n[-1]:
        print(f'Given list: {n}')
        print('result is True')
    else:
        print(f'y = {n}')
        print('result is False')

#Exercise5(y)


#Exercise 6: Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5

x = [10, 20, 33, 46, 55]
y = 5
def exercise6(x, y):
    print(f'Given list is {x}')
    print(f'Divisible by {y}')
    for i in x:
        if i % y == 0:
            print(i)

#exercise6(x, y)



#Exercise 7: Return the count of a given substring from a string
#Write a program to find how many times substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"

def exercise7():
    cnt = str_x.count("Emma")
    print(f'Emma appeared {cnt} times')

#exercise7()


#Exercise 8: Print the following pattern
#Output:

#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5
def exercise8():

    for num in range(6):
        for i in range(num):
            print (num, end=" ") #print number
        # new line after each row to display pattern correctly
        print("\n")


#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

y = 646


print(reverse(y))