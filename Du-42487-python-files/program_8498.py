def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   return a

def reverse(a):
   return a[::-1]

def main():
   a = [4, 3, 1, 2]
   i = 0
   j = 0
   while i < len(a):
      print(swap(a,2,3))
      return


if __name__ == "__main__":
   main()























































































































































































