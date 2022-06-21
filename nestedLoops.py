row = 7
#outer loop
for i in range(1, row + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')

#output
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * * * 
#* * * * * * * 

list_fruits = ['mango', 'apple', 'grapes', 'banana']
for fruit in list_fruits:
    for i in fruit:
        print(i, end='-')
    print()

#output:
#m-a-n-g-o-
#a-p-p-l-e-
#g-r-a-p-e-s-
#b-a-n-a-n-a-


color = ['red', 'green', 'blue']
items = ['apple', 'veggies', 'shirt']

for x in color:
    for y in items:
        print(x, y)

#output:
#red apple
#red veggies
#red shirt
#green apple
#green veggies
#green shirt
#blue apple
#blue veggies
#blue shirt


#Print right triangle

for i in range(11):
    for j in range(i):
        print("*", end=' ')
    print('')

#output:
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * * * 
#* * * * * * * 
#* * * * * * * * 
#* * * * * * * * * 
#* * * * * * * * * * 

#While loop - will keep iterating through the loop until it's true

i = 11
while(i > 0):
    j = 11
    while(j > i):
        print("*", end=' ')
        j = j-1
    i = i-1
    print()

#output:
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * * * 
#* * * * * * * 
#* * * * * * * * 
#* * * * * * * * * 
#* * * * * * * * * * 

#Append elements of 2 lists into empty list

list1 = [10, 25, 30]
list2 = [60, 15, 50]
result = []

for i in list1:
    for j in list2:
        result.append(i+j)
print(result)

#output:
# [70, 25, 60, 85, 40, 75, 90, 45, 80]


#Multiplying 2 lists
list3 = [2, 4, 6]
list4 = [2, 4, 6]
for i in list3:
    for j in list4:
        if i == j:
            continue
        print(i, '*', j, '= ', i*j)

#output:
#2 * 4 =  8
#2 * 6 =  12
#4 * 2 =  8
#4 * 6 =  24
#6 * 2 =  12
#6 * 4 =  24


# Perfect number - While Loop and For Loop
a = 1
while a <= 100:
    y_sum = 0
    for i in range(1, a):
        if a%i == 0:
            y_sum = y_sum + i
    if y_sum == a:
        print('Perfect number', a)
    a = a+1

#output:
#Perfect number 6
#Perfect number 28

fruits = ['apple', 'orange', 'kiwi']
for fruit in fruits:
    count = 0
    while count < 6:
        print(fruit, end = ' ')
        count = count+1

#output:
#apple apple apple apple apple apple orange orange orange orange orange orange kiwi kiwi kiwi kiwi kiwi kiwi %     