def swap(a, i, j):
 tmp = a[i] #temporary storage
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i): #can do y=1 then while and leave out x
   y = 1
   while y < len(a):
      y = y + 1
   return y

def sort(a):
   i = 0
   while i < len(a):
      y = find_position_of_smallest(a,i)
      swap(a,i,y) #reverses smallest for increasing
      i = i + 1
   return x
      



