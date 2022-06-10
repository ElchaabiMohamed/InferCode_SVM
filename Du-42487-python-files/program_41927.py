def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def find_position_of_smallest(a,i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   return p

def sort(a):
   i = 0
   while i < len(a):
      smallest = find_position_of_smallest(a,i)
      swap(a,i,smallest)
      i += 1
   return a

def main():
   print(sort([3, 2, 4, 1, 5, 3]))

if __name__ == "__main__":
   main()

