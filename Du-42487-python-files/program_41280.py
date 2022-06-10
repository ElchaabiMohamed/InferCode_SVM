def func_selection_sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + i
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1

      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i = i + 1

def main():
   a = [1, 5, 6, 2, 8]
   func_selection_sort(a)
   print(a[i])

if __name__ == "__main__":
   main()
