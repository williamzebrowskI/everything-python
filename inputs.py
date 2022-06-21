# input data

user_text = input('Enter some Text: ')

print(user_text.upper())

upper_or_lower = input('Enter 1 to uppercacse and 2 to lowercase: ')

#user_number = input('what do you want to doube? ')

#print(int(user_number) * 2)

if upper_or_lower == "1":
    print(user_text.upper())
if upper_or_lower == "2":
    print(user_text.lower())