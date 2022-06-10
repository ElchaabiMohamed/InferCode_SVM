def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p

def sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while i < len(j):
         if a[j] < a[p]:
            p = j
         j = j + 1
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i = i + 1

