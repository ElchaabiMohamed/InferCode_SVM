def selectionsort(a):

    i = 0
    while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
        if a[j] < a[p]:
          p = j
        j = j + 1

      
      tmp = a[p]  
      a[p] = a[i]
      a[i] = tmp
      # print (a[i])
      i = i + 1

import random

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()


# Unsorted: [85, 33, -69, 81, 51, 29, -60, 39, 59, -49]
# Sorted: [-69, -60, -49, 29, 33, 39, 51, 59, 81, 85]