a=[4,3,1,2]
def swap(a,i,j):
   tmp=a[i]
   a[i]=a[j]
   a[j]=tmp

def reverse(a):
   i=0
   j=len(a)
   while i<len(a)/2:
      swap(a,i,j)
      i=i+1
      j=j-1

