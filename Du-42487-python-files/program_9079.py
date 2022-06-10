def swap(a, i, j):

  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a, i):

  i = eval(input())
  j = 1
  while j < len(a):
    if a[i] < a[i + j]:
      i = i
    else:
      i = i + j
  j = j + 1

 
print(i)    
  
      
  


 

    
