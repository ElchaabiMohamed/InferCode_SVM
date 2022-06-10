def swap(a, i, j):
    temp = a[i]
    a[i] = a [j]
    a[j] = temp


def find_position_of_smallest(a,i):
   p = i
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p


def sort(a):
   b = a
   b = 0
   j = 1
   while j < len(a):
      if a[j] < a[b]:
         p = j
      j = j + 1

   return b
   
