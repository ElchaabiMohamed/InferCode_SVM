def swap(a, i, j):
 tmp = a[i] #temporary storage
 a[i] = a[j]
 a[j] = tmp

def find_position_of_smallest(a,i): #can do y=1 then while and leave out x
   s = i #s for selection sort/smallest
   while y < len(a):
      if a[i] < a[s]:
         s = i
      i = i + 1
   return s

def sort(a):
   i = 0
   while i < len(a):
      s = find_position_of_smallest(a,i)
      swap(a,i,s) #reverses smallest for increasing
      i = i + 1
   return s
      



