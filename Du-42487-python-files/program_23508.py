def quicksort(A, p, r):
  if r <= p:
    return #stops recursively
  q = partition(A, p, r)
  quicksort(A, p, q - 1)
  quicksort(A, q+1, r)

def partition(A, p, r):

    # q and j start at p
    q = j = p

    # up to but not including pivot
    while j < r:

        # move values less than or equal to pivot and update q
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1

        j += 1

    # swap pivot with A[q]
    A[q], A[r] = A[r], A[q]

    # return pivot index
    return q




import random

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    quicksort(A, 0, len(A)-1)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()
