# 4.1 If Statements


# 1:

def enterInt():
    x = int(input("Please Enter an Integer"))
    if x < 0:
        x = 0
        print('Negative Change to Zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
