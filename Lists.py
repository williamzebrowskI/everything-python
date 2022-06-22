from pkg_resources import cleanup_resources


fav_movies = ["Sandlot", "Luther", "Ted Lasso"]

#print(fav_movies[1]) # Prints number 1 movie, Luther

fav_movies.append("Iron Man") # Add's item to list, to the back of the list.


#print(len(fav_movies)) #len is getting the length of the list

fav_movies.insert(1, "Batman") #Insert item(string) into a specific spot of list 
#print(fav_movies)

del(fav_movies[2]) #delete item from a list 'del'

#print(fav_movies)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
b = []
def combine(lst):
    for i in lst:
        b.append(i)
    print(b)
#or
c = [x for x in a]

d = [1, 2, 3, 4, 5, 6, 7, 8]
e = [2, 4, 6, 8, 10, 12, 14, 16]

f = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
f1 = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
g = {i * j for i in d for j in e if j % 3 == 0}
h = {k: v for k, v in f.items() if v < 3 and k == 'a'}
i = {k: v for k, v in f.items() if v <= 1}
j = {v for v in f.values() if v >= 1}
k = {i * v for i in f.values() for v in f1.values()}
l = {k: v for k, v in f.items() for k, v in f1.items() if k > 'd'}

#print(l)






