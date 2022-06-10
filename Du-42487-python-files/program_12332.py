def selectionsort(a):
    for i in range(0, len(a)):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j = j + 1 
        tmp = a[p]
        a[p] = a[i]
        a[i] = tmp 
    
     