def bark():
    print("Woof woof!")

#bark()

#Parameters

def hello(name):
    print(f"Hello {name}")

#hello("Nick")

def add_numbers(num1, num2):
    print(num1 + num2)

#add_numbers(4, 8)



def dog_info(age, name):
    print(f"Your dogs name is {name} and he is {age} years old!")

#dog_info(2, 'Mark')


#Return informations

def double(number):
    return number * 2

#print(double(5))

# return text in all caps
def uppercase(text):
    return text.upper()

#print(uppercase('nick'))

names = ['tom', 'bill', 'boo']

#for name in names:
    #print(uppercase(name))


#for i in range(0, 101, 2):
    #print(i)


#Linear Search
#enumerate function which gives us both the index and value in a list
def linear_search(data, target):
    for idx, val in enumerate(data):
        if val == target:
            return idx  #Early exit if item is found
    return -1


#data = [4, 5, 2, 7, 1, 8]
#target = 1
#result = linear_search(data, target)
#if result == -1:
#    print("Item not found.")
#else:
#    print(f'Item found at position {result}.')




#itnerate through list and if value is greater than the one at min_index, update min_indez
#to the new positio

def selection_sort(xs): 
    for i in range(len(xs) - 1):     #THe last value will automatically be the orrect position
        min_idx = i            #Find minum value in unsorted region.
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[min_idx]:          #Update min_index if the value at j is lower than current minimum value.
                min_idx = j
        # After finding the minimum value in teh unsorted retion, swap with the first unsorted
        xs[i], xs[min_idx] = xs[min_idx], xs[i]

#xs = [3, 2, 1, 5, 4]
xs = [-4, 2, 5, 8, -7, 3, 6, -1, 7]
print(xs)
selection_sort(xs)
print(xs)


