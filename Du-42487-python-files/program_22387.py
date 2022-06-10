def partition(a, p, pivot):
   q = j = p

   while j < pivot:
      if a[j] <= a[pivot]:
         a[q], a[j] = a[j], a[q]
         q += 1
      j += 1

   a[q], a[pivot] = a[pivot], a[q]
   return q

def quicksort(a, p, pivot):
   
   if pivot <= p:
      return
   
   q = partition(a, p, pivot)
   quicksort(a, p, q-1)
   quicksort(a, q+1, pivot)