def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   while a[i] < a[i + 1]:
      print(a)
      a[i] = a[i + 1]
