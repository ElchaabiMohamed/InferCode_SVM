def selection_sort(a):                                # Sort list a.
   i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   swap(a,i,p)
   i = i + 1

