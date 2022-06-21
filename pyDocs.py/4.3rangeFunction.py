#4.3  The Range() Function:
#If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.
# It generates arithmetic progressions:

def range1():
    for i in range(5): 
        print(i)


list(range(5, 10))
list(range(0, 10, 2))
list(range(-10, -100, -30))



#To iterate over the indices of a sequence, you can combine range() and len() as follows:

a = ['Mary', 'had', 'a', 'little', 'lamb']
def interateRange():
    for i in range(len(a)):
        print(i, a[i])



range(10) #Output: range(0, 10)

sum(range(4)) # 0 + 1 + 2 + 3 -> Output: 6