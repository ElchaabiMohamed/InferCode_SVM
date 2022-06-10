def swap(a,i,j):
   
   temp = a[i]
   a[i] = a[j]
   a[j] = temp
   
   return

def find_position_of_smallest(a,i):
   
   answer = min(a[i:])
   a.index(answer)
   
   return



