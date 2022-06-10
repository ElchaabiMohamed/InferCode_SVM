def swap(a,i,j):
   a[i], a[j] = a[j], a[i]
   return a

def find_smallest_position(a,i):
   p = i
   j += 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1

   return p
def main():
   i = 0
   while i<len(a):
      p = find_smallest_position(a,i)
      swap(a, i, j)
      i += 1
   print(a)

if __name__ == "__main__":
   main()
