def bsearch(a, q):
   start = 0
   end = len(a)  
   while start < end:
      middle = (start + end) / 2
      if a[middle] < q:
         start = middle + 1
      else: 
         end = middle
   return start

