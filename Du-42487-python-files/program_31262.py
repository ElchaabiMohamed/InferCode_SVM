def selection_sort(a):
   j = 0
   while j < len(a):
      p = j
      i = j + 1
      while i < len(a):
         if a[i] < a[p]:
            p = i
         i = i + 1
 
      tmp = a[j]
      a[j] = a[p]
      a[p] = tmp
 
      j = j + 1

def main():
   a = [12, 5, 3, 6, 10, 11]
   selection_sort(a)
   print(a)

if __name__ == "__main__":
   main()