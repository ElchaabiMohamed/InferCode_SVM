


def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
  i=0
  while i < len(a)/2:
    tmp = a[i]
    a[i]= a[len(a)-i-1]
    a[len(a)-i-1]=tmp
    i=i+1

  
