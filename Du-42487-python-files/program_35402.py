def selection_sort(a):
    while j<len(a):
        if a[j]<a[p]:
            p=j
        j=j+1
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
    
    i=0
    while i<len(a):
       p=i
       j=i+1
       smallest(a,j,p)
       swap(a,i,p)
       i+=1
