def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = a[i]

def reverse(a):
   i = 0
   while i < (len(a)/2):
      a = swap(a,i,(len(a)-i))
      i = i + 1
   
if __name__ == "__main__":
   main()
