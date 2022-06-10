a=[]

def selection_sort(a):
   i=0
   while i<len(a):
    p=i
    j=i+1
    while j<len(a):
     if a[j]<a[p]:
       p=i
       tmp=a[p]
       a[p]=a[j]
       a[j]=tmp
     j+=1
    i+=1
 
