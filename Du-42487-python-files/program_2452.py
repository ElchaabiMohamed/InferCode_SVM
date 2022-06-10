def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   k = 0
   while k < (len(a)/2):
      a = swap(a,k,(len(a)-i))
      k = k + 1
   return a

def main():
   a = [4,3,1,2]
   swap(a,2,3)
   print(a)
   reverse(a)
   print(a)

if __name__ == "__main__":
   main()
