a = (1, 2, 3, 4)
def swap(a,i,j):
 tmp = a[i]
 a[i] = a[j]
 a[j] = tmp 

def find_position_of_smallest(a,i):
 p = i 
 j = i 
 while j < len(a): 
     if a[j] < a[p]:
        p = j 
     j = j + 1
 return p
