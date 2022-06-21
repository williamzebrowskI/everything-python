def main():
    
    seq = range(11)
    seq2 = [x * 2 for x in seq]  #prints each number x 2.
    seq3 = [x for x in seq if x % 3 != 0]  #printing list of numbers NOT divisable by 3
    seq4 = [(x, x**2) for x in seq]  # a list of each element of the sequence squared. 

    from math import pi
    seq5 = [round(pi, i) for i in seq]  # pi rounded to the number of places for each number in the seq.

    seq6 = { x: x**2 for x in seq } # Create a dictionary, a dictionary for each element and it's sqaured

    seq7 = {x for x in 'superduper' if x not in 'pd'}  #set of all letters of string superduper that are not 'pd'

    print_list(seq)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


