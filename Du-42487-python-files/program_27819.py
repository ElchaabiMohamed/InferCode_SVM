def swap(a, i, j):
 tmp = a[i] #temporary storage
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i): #can do j=1 then while and leave out p
   x = i
   y = i + 1
   while y < len(a):
      if a[y] < a[x]:
         x = y
      y = y + 1
   return x

def sort(a):
   i = 0
   while i < len(a):
      x = find_position_of_smallest(a,i)
      swap(a,i,x) #reverses smallest for increasing
      i = i + 1
   return x
      



