def quicksort(a):
    less = []
    equal = []
    greater = []

    if len(a) > 1:
        pivot = a[0]
        for x in a:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return a

import random

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    quicksort(A, 0, len(A)-1)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()