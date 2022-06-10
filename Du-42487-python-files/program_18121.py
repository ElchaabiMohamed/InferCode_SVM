def selection_sort(a):
    i=0
    j=0
    p=0
    while j<len(a):
        if a[j]<a[p]:
            p=j
        j=j+1
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
    while i<len(a):
       p=i
       j=i+1
       smallest(a,j,p)
       swap(a,i,p)
       i+=1
