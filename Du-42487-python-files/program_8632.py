def selectionsort(A):
    recursive_selectionsort(A, 0)

def recursive_selectionsort(A,i):
    if i >= len(a) - 1:
        return
    else:
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j = j + 1

        tmp = a[p]
        a[p] = a[i]
        a[i] = tmp

        recursive_selectionsort(A, i+1)

a = [3,4,2,1,5]

selectionsort(a)
print(a)
