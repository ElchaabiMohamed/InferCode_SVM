def partition(a, start, pivot):
   lower = upper = start

   while upper < pivot:
      if a[upper] <= a[pivot]:
         a[lower], a[upper] = a[upper], a[lower]
         lower += 1
      upper += 1

   a[lower], a[pivot] = a[pivot], a[lower]
   return lower

def quicksort(a, start, pivot):
   
   if pivot <= start:
      return
   
   lower = partition(a, start, pivot)
   quicksort(a, start, lower-1)
   quicksort(a, lower+1, pivot)