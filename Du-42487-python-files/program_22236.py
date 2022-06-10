def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   if a[i] < a[i+1] or a[i+2] or a[i+3]:
      return a[i]
   elif a[i+1] < a[i+2] or a[i+3]:
      return a[i+1]
   elif a[i+2] < a[i+3]:
      return a[i+2]
   else: 
      return a[i+3]
