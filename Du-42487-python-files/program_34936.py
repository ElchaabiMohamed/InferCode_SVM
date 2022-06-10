def selection_sort(a):
   import func_reverse
   i = 0
   while i < len(a):
      j = i
      while j < len(a):
         if a[j] < a[i]:
            swap(a, i, j)
      i = i + 1

def main():
   print(a)

if __name__ == "__main__":
   main()
