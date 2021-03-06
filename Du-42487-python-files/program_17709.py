def selectionsort(n):
  i = 0
  while i < len(n):
    position = i
    j = i + 1
    while j < len(n):
      if n[j] < n[position]:
        position = j
      j = j + 1
    val = n[position]
    n[position] = n[i]
    n[i] = val  
    i = i + 1
import random

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()

"""
def partition(A, p, r):

  # q and j start at p (position)
  q = j = p
  # up to but not including pivot r
  while j < r:
    # move values less than or equal to pivot "r" and update "q"
    if A[j] <= A[r]:
      A[q], A[j] = A[j], A[q]
      q += 1
    j += 1

  # swap pivot r with A[q]
  A[q], A[r] = A[r], A[q]
  # return pivot index
  return q


def selectionsort(A, p, r):
  if r <= p:
    return

  q = partition(A, p, r)
  quicksort(A, p, q-1)
  quicksort(A, q+1, r)



import random

def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    quicksort(A, 0, len(A)-1)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()
"""
