def swap(a,i,j):
   tmp=a[i]
   a[i]=[j]
   a[j]=tmp
   return a

def reverse(a):
   i=0
   while i<len(a):
     tmp=a[i]
     a[i]=[len(a)-i-1]
     a[len(a)-i-1]=tmp
     i=i+1
   return a
