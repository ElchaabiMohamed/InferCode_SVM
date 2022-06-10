def minimum(l):
    
    def quicksort(A, p, r):
        #Base Case
        if r <= p:
            return

        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

    def partition(A, p, r):
        q = j = p

        #up to but not including pivot
        while j < r:

            if A[j] <= A[r]:
                A[q], A[j] = A[j], A[q]
                q += 1

            j += 1

        A[q], A[r] = A[r], A[q]

        return q


    quicksort(l, 0, len(l)-1)
    return l[0]

    

    