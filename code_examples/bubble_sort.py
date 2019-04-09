# Exercise Bubble sort
# Create the code for a function that uses the bubble sort algorithm


def bubble_sort(l):
    swap = False # if the list is iterated through 1 time without swap then it is sorted
    while not swap:
        print('bubble sort: ' + str(l))
        swap = True
        for j in range(1, len(l)):
            if l[j-1] > l[j]:
                swap = False
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp

test_list = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(test_list))
print(test_list)