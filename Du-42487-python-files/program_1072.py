
def selection_sort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1                                 
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1
      tmp = a[i]
      a[i] = a[p]
      a[p] = tmp
      i = i +1
   return a

def main():
   a=[5,4,3,2]

   selection_sort(a)
   print(a)
if __name__ == "__main__":
   main()
