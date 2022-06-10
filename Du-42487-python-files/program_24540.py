
def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      j = i
      while j < len(a):
         if a[j] < a[i]:
            swap(a,i, j)
         j = j + 1
      i = i + 1

def main():
   selection_sort(a)
   print(a)

if __name__ == "__main__":
   main()
