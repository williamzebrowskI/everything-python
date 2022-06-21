

def main():
    f = open('notes.txt', 'rt')  #opens the file and returns a file object / 'r' is read mode
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()


#   \n = new line
# exp:  x = 'String\n'
