def swap(a, i, j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp 

def reverse(a):
   i = 0
   j = len(a) - 1
   while i <= j:
      swap(a, i, j)
      i = i + 1
      j = j - 1 

def main():

   a = [4, 3, 1, 2]
   b = [4, 3, 1, 2]
   swap(a, 1, 2)
   print(a)
   reverse(b)
   print(b)
 
if __name__ == "__main__":
   main()
