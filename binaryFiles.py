def main():
    infile = open('berlin.jpg', 'rb')  #opens the file and returns a file object / 'r' is read mode / 'b' is file type
    outfile = open('berlin-copy.jpg', 'wt')  #writes file
    while True:
        buf = infile.read(10230)
        if buf:
            outfile.write(buf)
            print('.', end= ' ', flush=True)
        else: break
        outfile.close()
        print('\ndone.')

if __name__ == '__main__': main()