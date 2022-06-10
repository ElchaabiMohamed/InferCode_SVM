def selectionsort(n):
   i = 0
   while i < len(n):
      p = i
      j = i + 1
      while j < len(n):
         if n[j] < n[p]:
            p = j
         j = j + 1

      temp= n[p]
      n[p] = n[i]
      n[i] = temp

      i = i + 1

import random
def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()
