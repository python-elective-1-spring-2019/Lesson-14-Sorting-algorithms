# Traverse through 1 to len(l) 

def insertion_sort(l):

    for i in range(1, len(l)): 

        key = l[i] 
                   
        # Move elements of l[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1 # 1) = 0
                # 2) = 1
        while j >= 0 and key < l[j] : 
                l[j + 1] = l[j] # swap l[1] with l[0]
                j -= 1 # = -1
        l[j + 1] = key # l[0] = 11
  
  
# Driver code to test above 
l = [12, 11, 13, 5, 6] 
# 2) l = [11, 12, 13, 5, 6]
insertion_sort(l) 

for i in range(len(l)): 
    print (f'{l[i]}') 
