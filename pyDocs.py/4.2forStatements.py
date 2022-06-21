# 4.2
# Python’s for statement iterates over the items of any sequence (a list or a string), 
# in the order that they appear in the sequence. 

words = ['cat', 'dog', 'horse', 'elephant', 'pinnochio']

def lenWords():
    for w in words: print(w, len(w))


# Code that modifies a collection while iterating over that same collection can be tricky to get right. 
# Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

users = {'Hans': 'active', 'Billy': 'inactive', 'Noopy': 'active', 'Shriky': 'inactive'}

# Strategy:  Iterate over a copy

def copyCollection():
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

# Strategy:  Create a new collection
new_users = {}
def newCollection():
    for user, status in users.items():
        if status == 'active':
            new_users[user] = status

#print(new_users)
