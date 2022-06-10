
import random

def selectionsort(a):
    a = a[:]
    out = []

    while a:
        smallest = min(a)
        a.remove(smallest)
        out.append(smallest)

    return out
def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()