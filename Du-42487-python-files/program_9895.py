a=[]
i=0

def swap(a,i,j):
   tmp=a[j]
   a[j]=a[i]
   a[i]=tmp
   
def find_position_of_smallest(a,i):
   if a[i] > a[i+1]:
    a[i] = a[i]
   else:
    a[i]=a[i+1]
