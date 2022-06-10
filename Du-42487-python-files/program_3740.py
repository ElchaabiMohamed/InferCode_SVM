def selection_sort(a):
    i=0
    while i<len(a):
        p=a[i]
        j=i+1
        while j<len(a):
            if a[j]<a[p]:
                p=j
            j=j+1
        tmp=a[i]
        a[i]=a[p]
        a[p]=tmp
        i=i+1
    return a
def test():
    return selection_sort(2)
if "__name__"=="__main__":
    test()