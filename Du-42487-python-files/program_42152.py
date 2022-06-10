def swap(a,i,j):
   a[i], a[j] = a[j], a[i]
   return a

def reverse(a):
   return a[::-1]

def main():
   a = [4, 3, 1, 2]
   
   print((swap(a,2,3)))
   print((reverse(a)))


if __name__ == "__main__":
   main()


