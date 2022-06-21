import sys

def main():
    try:
        #x = int('fool')
        x = 5/0
    except ValueError:
        print('I caught a Value Error')
    except ZeroDivisionError:
        print('don\'t devide by zero')
    except:                           #default except that does not know what error it is.
        print(f'unknown error: {sys.exc_info()[1]}')    #We can call sys to print the traceback error and [1] for the exact reason
    else:     # only executed if you dont have an error
        print('Good Job')
        print(x)

if __name__ == '__main__': main()

#the ValueError that is generated in the console is a token is the name of the type of the error.  
# You can check this by checking the expression


