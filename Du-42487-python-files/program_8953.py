def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1 

      swap(a, i, p)

      i = i + 1
   return a 

def main():
   a = [3, 5, 2, 6]
   print(selection_sort(a))

if __name__ == "__main__":
   main()



