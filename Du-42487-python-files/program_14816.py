def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp
   return a

def reverse(a):
   n = len(a)
   i = 0
   while i < n/2:
      tmp = a[i]
      a[i] = a[len(a)-i-1]
      a[len(a)-i-1] = tmp
      i = i + 1
   return a

def main():
   a = [1,2,3,4]
   i = 2
   j = 3
   print(swap(a,i,j))
   print(reverse(a))

if __name__ == "__main__":
   main()
