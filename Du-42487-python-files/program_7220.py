def selectionsort(a):
    for i in range(len(a)):
        j = i + 1
        p = i
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j += 1
        a[p], a[i] = a[i], a[p]
