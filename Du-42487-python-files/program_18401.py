def selection_sort(a):
   i = 0
   n = len(a)
   while i < n:
      p = i
      j = i + 1
      while j < n:
        if a[j] < a[p]:
           p = j
        j = j + 1
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i = i + 1
   return a

def main():
   a = [9,4,8,3,7,2,6,5,1]
   print(selection_sort(a))

if __name__ == "__main__":
   main()
