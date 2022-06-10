def selection_sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i = i + 1
   return a


def main():
   a = [1, 2, 3, 1, 2, 3]
   print(selection_sort(a))

if __name__ == "__main__":
   main()