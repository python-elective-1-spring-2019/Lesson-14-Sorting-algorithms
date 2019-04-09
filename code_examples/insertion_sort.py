# Traverse through 1 to len(l) 

def insertion_sort(l):

    for i in range(1, len(l)): 

        key = l[i] # l[3]  = 5

        j = i-1 # 2
        
        while j >= 0 and key < l[j]: # 5 < 13
                l[j + 1] = l[j] 
                j -= 1 # j=1
        l[j + 1] = key 
  
  
# Driver code to test above 
#l = [12, 11, 13, 5, 6] '
l = [11, 12, 13, 5, 6, 5, 7 ,10, 44, 66, 77, 2, 3, 888, 9, 6,53495346875 ] 
insertion_sort(l) 
for i in range(len(l)): 
    print (f'{l[i]}', end=' ') 

print()
