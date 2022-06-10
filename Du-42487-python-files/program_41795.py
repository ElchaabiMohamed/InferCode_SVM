import random


def selectionsort(a):
    for i in range(len(a)):
        least = i
        for k in range(i + 1, len(a)):
            if a[k] < a[least]:
                least = k

        swap(a, least, i)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp



def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))


if __name__ == '__main__':
    main()
