def swap (a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   n = eval(input())
   i = 0
   j = 0
   while i < len(a):
      if a[i] < a[j]:
         j = i
   i = i + 1
   return (a,j)
