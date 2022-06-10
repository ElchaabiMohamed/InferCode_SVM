
def selection_sort(a):
    i = 0
    while i < len(a):
        j = i
        k = i
        while k < len(a):
            if a[j] > a[k]:
              k = j
            k = k + 1

        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
       
        i = i + 1

    return a