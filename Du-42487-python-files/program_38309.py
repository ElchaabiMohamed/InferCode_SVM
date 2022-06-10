def selectionsort(array):
    def chksorted(a):
        for i in range(len(a)-1):
            if not a[i] < a[i+1]:
                return False
        return True
    m = min(array)
    mi = array.index(m)
    if not chksorted(array):
        f = array[0]
        array[0] = m
        array[mi] = f
