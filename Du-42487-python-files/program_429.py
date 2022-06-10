import random

def selectionsort(a):
   i = 0
   p = 0
   while i < len(a): 
      p = i # if value at i is less than start value swap p and i
      j = i + 1 #j is value one ahead of the sorted list
      while j < len(a):
         if a[j] < a[p]: #first element of unsorted list is less than position p 
            p = j 
         j = j + 1
      
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i = i + 1
   return(a)
def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()
