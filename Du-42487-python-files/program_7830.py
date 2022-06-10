def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
    return a
def reverse(a):
    i=0
    while i<len(a)/2:
        tmp=a[i]
        a[i]=a[len(a)-1-i]
        a[len(a)-1-i]=tmp
        i=i+1
    return a
def test():
    swap(2)
    reverse(2)
if "__name__"=="__main__":
    main()