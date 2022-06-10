def quicksort(A, p, r):
   #base case
   if r <= p:
      return
   q = partition(A, p, r)
   quicksort(A, p, q - 1)
   quicksort(A, q + 1, r)

def partition(A, p, r):
   #initilise q and j:
   q = j = p
   #up to but not including pivot:
   while j < r:
      #A[j] not in right position:
      if A[j] <= A[r]:
         #swap A[j] with A[q]
         A[q], A[j] = A[j], A[q]
         q += 1
      j += 1
   A[q], A[r] = A[r], A[q]
   return q



#from quicksort_102 import quicksort
import random

def main():
   A = random.sample(list(range(-99, 100)), 10)

   print(('Unsorted: {}'.format(A)))
   quicksort(A, 0, len(A)-1)
   print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
   main()
