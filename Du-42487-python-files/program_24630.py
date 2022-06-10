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
   
   mid = partition(a, start, pivot)
   quicksort(a, start, mid-1)
   quicksort(a, mid+1, pivot)