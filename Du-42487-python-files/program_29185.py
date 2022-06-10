def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   z = 0
   x = len(a)
   if len(a) % 2 != 0:
      while z < len(a)/ 2:
         swap(a,z,x)
         z = z + 1
         x = x - 1
   else:
      while z < len(a)/2 + 1:
         swap(a,z,x)
         z = z + 1
         x = x - 1