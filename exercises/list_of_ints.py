"""
Exercise: create a function that takes an int parameter. 
Generate an unordered list of the lenght of the parameter.
Run a script like word_count.py where you use this module to 
generate lists and test the algorithms we worked and will work with
"""
import sys
import random


def list_of_ints(num):
    """ Generates an unordered list of ints of the length of 'num'
        Takes a number parameter
        Returns: lists of unordered numbers where all numbers from 0-num are represented """

    # Exercise: Generate a list of length len(num) containing all numbers from 0 - len(num)-1
    # The numbers should NOT be in order 0, 1, 2, 3, 4 etc. It should be an unordered list.
    # You can use the random module, but not the method "shuffle" from that module.
    # You should instead make your own "shuffle"

    pass


def main():
    try:
        lst = list_of_ints(int(sys.argv[1]))
        print(lst)
    except IndexError:
        print('You need to specify the an argument (length of the list to be generated)')
        print('ie. ($ python list_of_ints.py 100)')


if __name__ == "__main__":
    main()
