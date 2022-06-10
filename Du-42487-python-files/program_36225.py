def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      j = i + 1
      p = i
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1
      swap(a,i,p)
      i = i + 1
   return a