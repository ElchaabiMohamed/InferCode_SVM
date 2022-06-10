def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(a,i,len(a)-i-1)
      i += 1

def main():
   a = [4, 3, 2, 1]
   print(reverse(a))


if __name__ == "__main__":
   main()
