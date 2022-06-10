def swap(a,i,j):
   a[i]=tmp
   a[j]=a[i]
   tmp=a[j]
def reverse(a,i,j):
   i=0
   j=len(a)-1
   while i<len(a):
      swap(a,i,j)
      i+=1
      j-=1
