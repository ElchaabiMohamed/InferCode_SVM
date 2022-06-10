import random


def selectionsort(a):
    a = a[:]
    sortedlist = []
    while a:
        smallest = min(a)
        a.remove(smallest)
        sortedlist.append(smallest)

    return sortedlist




def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(selectionsort(A))))


if __name__ == '__main__':
    main()
