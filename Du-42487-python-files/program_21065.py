a=[]
def smallest(a,j,p):
    while j<len(a):
        if a[j]<a[p]:
            p=j
        j=j+1
def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
i=0
while i<len(a):
    p=i
    j=i+1
    smallest(a,j,p)
    swap(a,i,j)
    i+=1
