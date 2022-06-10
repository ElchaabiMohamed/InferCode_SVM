def selectionsort(a):
   for i in range(len(a)):
      for j in range(i + 1, len(a)):
         if (a[i] > a[j]):
            a[i], a[j] = a[j], a[i]

   return a

import random

def main():
   A = random.sample(list(range(-99, 100)), 10)

   print(('Unsorted: {}'.format(A)))
   selectionsort(A)
   print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
   main()