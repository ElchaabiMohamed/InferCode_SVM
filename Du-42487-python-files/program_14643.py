def selection_sort(a):
   i=0
   while i<len(a):
      smallest=0
      j=1
      while j<len(a):
         if a[j]<a[smallest]:
            smallest=j
         j=j+1
      tmp = a[0]
      a[0] = a[smallest]
      a[smallest] = tmp
      i=i+1
