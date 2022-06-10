def selection_sort(a):
   i = 0
   while i < len(a):
      small = i
      j = small + 1
      while j < len(a):
         if a[j] < a[small]:
            small = j
         j += 1
      tmp = a[small]
      a[small] = a[i]
      a[i] = tmp  
      i += 1
