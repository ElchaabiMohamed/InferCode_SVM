def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = 0
   while i < (len(a)/2):
      swap(a,i,(len(a)-1))
      i = i + 1
   return a

def main():
   a = [4,3,2,1]
   a = swap(a,2,3)
   print(a)
   a = reverse(a)
   print(a)

if __name__ == "__main__":
   main()
