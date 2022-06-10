def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest9(a,i):
   i = 0   
   p = i
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   

