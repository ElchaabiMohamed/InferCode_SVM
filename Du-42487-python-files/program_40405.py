def quicksort(A, beg, end):
    if end - beg < 1:
        return

    i = j = beg
    while i <= end:
        if A[i] <= A[end]:
            A[i], A[j] = A[j], A[i]
            j += 1
        i += 1

    quicksort(A, beg, j - 2)
    quicksort(A, j, end)

import random

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    quicksort(A, 0, len(A)-1)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()
