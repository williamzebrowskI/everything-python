def main():
    infile = open('notes.txt', 'rt')  #opens the file and returns a file object / 'r' is read mode
    outfile = open('notewrite.txt', 'wt')  #writes file
    for line in infile:
        print(line.rstrip(), file=outfile) # each line is print into new file outfile.
        print('.', end= ' ', flush=True)
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()