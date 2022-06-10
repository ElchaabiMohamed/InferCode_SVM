def selection_sort(a):
   i = 0
   while i < len(a):
      j = i
      while j < len(a):
         if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
         j += 1
      i += 1
   return a

def main():
   print(selection_sort(a))
   
if __name__ == "__main__":
   main()
