def selectionsort(l):
   i = 0
   while i < len(l):
      p = i
      j = i + 1
      while j < len(l):
         if l[j] < l[p]:
            p = j
         j = j + 1

      tmp = l[p]
      l[p] = l[i]
      l[i] = tmp

      i = i + 1

#from selectionsort_102 import selectionsort
import random

def main():
   A = random.sample(list(range(-99, 100)), 10)

   print(('Unsorted: {}'.format(A)))
   selectionsort(A)
   print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
   main()