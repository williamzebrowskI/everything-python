number_list = [ x for x in range(20) if x % 2 == 0]

#print(number_list)

y = 'HeLlO WoRlD!'
f = [x for x in y if x.isupper()]   #prints out only uppercase letters in new list.

#print(f)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
f = [x for x in fruits if 'a' in x]   # prints out a word if it has an 'a' in the word
print(f)


h= []
for x in range(30):
    if x % 2 == 0:
        h.append(x)
#print(h)


y = [x for x in range(30) if x % 2 == 0]
#print(y)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
#print(num_list)

nums = [y for y in range(1, 200) if y % 4 == 0]
#print(nums)

