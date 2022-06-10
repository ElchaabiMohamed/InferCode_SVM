def swap(a,i,j):   # Swap the elements at positions i and j in list a.
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp

def find_smallest_position(a,i):   # Return the position of the smallest element in a[i:].
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   return p	

def selection_sort(a):   # Sort list a using the selection-sort algorithm.
   i = 0
   while i < len(a):
      p = find_smallest_position(a,i)
      swap(a,i,p)
      i = i + 1
   return a   
   

def main():
   a = [1, 2, 3, 1, 2, 3]
   print(selection_sort(a))


if __name__ == "__main__":
   main()   