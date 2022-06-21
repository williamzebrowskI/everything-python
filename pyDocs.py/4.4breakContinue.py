#4.4. break and continue Statements, and else Clauses on Loops

#The break statement, like in C, breaks out of the innermost enclosing for or while loop.

# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion 
# of the iterable (with for) or when the condition becomes false (with while), but not when the loop
# is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers:

def primeNumber():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through w/o finding a factor
            print(n, 'is the prime number')



def fibernocci():
    a, b = 0, 1
    while a < 1000000:
        print(a)
        a, b = b, a+b
