def selectionsort(l):
    for i in range(len(l)):
        j = i + 1
        p = i
        while j < len(l):
            if l[j] < l[p]:
                p = j
            j += 1
        l[p], l[i] = l[i], l[p]
