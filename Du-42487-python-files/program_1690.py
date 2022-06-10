def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp
  
def find_smallest(a,i):
  p = i 
  j = i + 1
  while j < len(a):
    if a[j] < a[p]:
      p = j
    j = j + 1
  return p
  
def selection_sort(a):
  i = 0
  while i < len(a):
    p = find_smallest(a,i)
    swap(a,i,p)
    i = i + 1
    
     
    