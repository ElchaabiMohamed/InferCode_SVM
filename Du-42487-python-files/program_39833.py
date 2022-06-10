def selection_sort(a):
   i= 0
   p =0
   j = 1
   while i < len(a):
    if a[j] < a[p]:
      p = j
    j = j+1
    i = i + 1
