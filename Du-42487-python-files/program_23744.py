def selection_sort(a):
   i = 0
   j = 1
   while i < len(a):
      j = i
      while j < len(a):
         if a[j] < a[i]:
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp
         j = j + 1
      i = i + 1
