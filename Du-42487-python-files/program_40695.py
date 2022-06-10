def swap(a, i, j):
 tmp = a[i] #temporary storage
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i): #can do j=1 then while and leave out p
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   return p

def sort(a):
   i = 0
   while i < len(a):
      p = find_position_of_smallest(a,i)
      swap(a,i,p) #reverses smallest for increasing
      i = i + 1
   return p
      



