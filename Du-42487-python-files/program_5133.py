def find_smallest(a,i):
   p = i
   q = i + 1
   while q < len(a):
      if a[q] < a [p]:
         p = q
      q += 1
   return p

def swap(a,i,p):
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp   

def selection_sort(a):
   i=0
   while i < len(a):
      p = find_smallest(a, i)
      swap(a,i,p)      
      i += 1

def main():
   list = [3,6,32,4]
   selection_sort(list)
   print(list)

if __name__ == "__main__":
   main()