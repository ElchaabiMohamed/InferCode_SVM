
# a = ["i", "j"]
def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   i = i + 1
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   return p

def sort(a):
   x = int(a[0])
   i = 0
   while i < len(a) - 1:
      if int(a[i]) > int(a[i+1]):
         x = a[i]
         a[i] = a[i + 1]
         a[i+1] = x
      i = i + 1

   i = 0
   while i < len(a):
      print(a[i])
      i = i + 1


