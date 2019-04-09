"""
Exercise: create a function that takes an int parameter. 
Generate an unordered list of the lenght of the parameter.
Run a script like word_count.py where you use this module to 
generate lists and test the algorithms we worked and will work with
"""
import sys
import random
import time

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            return False
    return True


def bogo_sort(l):
    while not is_sorted(l):
        random.shuffle(l)
    
    print(l)


def list_of_ints(num):
    """ Generates an unordered list of ints of the length of 'num'
        Takes a number parameter
        Returns: lists of unordered numbers where all numbers from 0-num are represented """

    list = []
    for i in range(num):
        list.append(i)

    for i in range(1, len(list)):
        temp_1 = random.randint(0, i)
        temp_2 = random.randint(0, i)
        list[temp_1], list[temp_2] = list[temp_2], list[temp_1]

    return list


def list_of_tobias(num):
    list = []
    i = 0
    while i < num:
        rand = random.randint(1, num)
        if rand not in list:
            list.append(rand)
            i += 1

    return list


def main():
    
    
    bogo_sort([2, 3, 1, 10, 33, 22, 66, 44, 11, 22, 33])
    
    
    try:
        # ===  2 times for loops
        start = time.time()
        lst = list_of_ints(int(sys.argv[1]))
        end = time.time()
        #print(lst)
        print('The list_of_ints execusion time was',
              format(end - start, '.6f'), 'seconds')

        # ===  while loop
        start = time.time()
        lst = list_of_tobias(int(sys.argv[1]))
        end = time.time()
        #print(lst)
        print('The list_of_tobias execusion time was',
              format(end - start, '.6f'), 'seconds')



    except IndexError:
        print('You need to specify the an argument (length of the list to be generated)')
        print('ie. ($ python list_of_ints.py 100)')


if __name__ == "__main__":
    main()
