#!/usr/bin/ python3   # Shebang allows a script to be invoked from the command line.  

# /usr/local/bin/python  # you can use the aboslute path to the python interpreter. 


import platform

print('This is python version {}'.format(platform.python_version()))

#Alternate

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()