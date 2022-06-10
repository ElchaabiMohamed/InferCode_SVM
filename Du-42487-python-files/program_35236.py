def swap(a, i, j):
   temp = a[i]
   a[i] = a[j]
   a[j] = temp
   
def find_position_of_smallest(a, i):
   x = i
   while i < len(a):
      if a[i] < a[x]:
         x = i
      i = i + 1
   return x   

def sort(a):
   j = 0
   while j < len(a):
     p = find_position_of_smallest(a, j)
     swap (a, j, p)
     j = j + 1
