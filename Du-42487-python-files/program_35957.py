def partition(a, start, pivot):
   lower = upper = start # Initialize indexes

   while upper < pivot: # While part of list remains un-processed
      if a[upper] <= a[pivot]: 
         a[lower], a[upper] = a[upper], a[lower] # If upper element is less than pivot, swap with lower element
         lower += 1 # Increase lower index
      upper += 1 # Increase upper index

   a[lower], a[pivot] = a[pivot], a[lower] # Place pivot between partitioned sections
   return lower # Return position that pivot is placed

def quicksort(a, start, pivot):
   
   if pivot <= start: # Keep sorting while sections to be sorted are at least 2 elements long
      return
   
   mid = partition(a, start, pivot) # Partition the list
   quicksort(a, start, mid-1) # Sort lower part
   quicksort(a, mid+1, pivot) # Sort higher part