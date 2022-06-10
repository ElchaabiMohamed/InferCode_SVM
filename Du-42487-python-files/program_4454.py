def swap(a,i,j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = 0
   while i < len(a)/2:
      tmp = a[i]
      a[i] = a[len(a) - i - 1]
      a[len(a) - i - 1] = tmp
      i = i + 1

def main():
   a = [12, 5, 3, 6, 10, 11]
   reverse(a)
   print(a)

if __name__ == "__main__":
   main()