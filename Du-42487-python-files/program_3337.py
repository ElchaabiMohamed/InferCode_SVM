def swap(a, i, j):

  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a, i):

  j = i
  while i < len(a):
    if a[i] < a[j]:
      j = i
    i = i + 1

  return j

def sort(a):

  i = 0
  j = i

  while i < len(a):
    if a[i] < a[j]:
      j = i
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
  i = i + 1


 
   
  
      
  


 

    
