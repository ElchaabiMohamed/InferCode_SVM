def selection_sort(a):

   while i < len(a):
      j = i + 1
      i = 0
      p = i
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1


      tmp = a[i]
      a[i] = a[p]
      a[p] = tmp


      i = i + 1
   
   return a
      
   