d = {}  #Create an empty dictionary

d = {"I":1, "II":2, "III":3 } #Add three items in a dictionary

d["IV"]=4 #add an etry

del d['IV'] # delete an etry

len(d) #length of dictionary

d.clear() #empty dictionary

d=dict() # dict: creates an new dictionary


if ('II' in d):   #Function working with dictionary
    print(d['II'])
else:
    print("not found")

for number in d:
    print(d[number])

d = {"I":1, "II":2, "III":3 }
print(d)

if ("IV" not in d):
    d["IV"]=4
else:
    print("key exists")

print(d)

print (d.get ('IV', "not found"))  # get value of key -returns 4
print (d.get ('X', "not found"))  # no value found because there is no key called X

d.keys() # List all keys

d.values() # List all values

d.items() # List both keys and values

#d.max() # returns keys which has the largest value in dict

#d.min() # returns keys which has the smallest value in dict

#d.pop() # returns the value associated with key, and removes the key-value pair from dict

#d.sorted() # sorts list

print( sorted(d.keys()))

d.copy() # makes a copy - used carefully


eng_di={}
#Adding lists as value
eng_di
#Creating a dictionary with an empty list

eng_di.clear()


square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)


orig = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in orig.items() if v % 2 == 0}
new_dict = {k: v for (k, v) in orig.items() if v % 2 != 0 if v > 10}
new1 = {k: v for (k, v) in orig.items()}
print(new1)
print(even_dict)
print(new_dict)

#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dtop = 0.76
new_price = {k: v*dtop for (k, v) in old_price.items()}
print(new_price)

sold = {'towels': 10, 'coffee': 30, 'bread': 6}
t = {k: v for (k, v) in sold.items() if v >= 5 if 'o' in k}
b = {k: v for (k, v) in sold.items() }
print(t)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young') for (k, v) in original_dict.items()}
print(new_dict_1)

inputs = "noodles, rice, banan, sweets, ramen, souffle, apricot, apple, bread"

y = [x for x in inputs if x[0] == inputs[0]]
print(y)