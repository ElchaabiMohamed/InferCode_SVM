import random

def selectionsort(A):
    i = 0
    while i < len(A):
        j = i + 1
        while j < len(A):
            if A[j] < A[i]:
                A[j], A[i] = A[i], A[j]
            j += 1
        i += 1
    return A
    

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()