a=[]
i=0

def swap(a,i,j):
   tmp=a[j]
   a[j]=a[i]
   a[i]=tmp
   
def find_position_of_smallest(a,i):
   p = j
   
   while j < len(a):
      if a[j] < a[p]:
         p=j
      j = j + 1
   return p
   
