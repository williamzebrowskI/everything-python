for number in range(1):  #runs Hello 10 times, loops through each number in the range
    print('Hello')
    print(number)



fav_movies = ["Sandlot", "Luther", "Ted Lasso"]

for movie in fav_movies:
    print(movie)

c = [x*2 for x in range(2)]
print(c)



#while loop
words = ['one', 'two', 'three', 'four', 'five']

n=0

while (n < 5):
    print(words[n])
    n +=1 


#simple fibonacci series
a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a+b

print()



#for loop

words = ['one', 'two', 'three', 'four', 'five']
for i in words:
    print(i)