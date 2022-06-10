def swap(a,i,j):
   a[i], a[j] = a[j], a[i]
   return a

def reverse(a):
   i = len(a)-1
   new_array = []
   while i >= 0:
      new_array.append(a[i])
      i -= 1

   return new_array

def main():
   a = [4, 3, 1, 2]
   
   print((swap(a,2,3)))
   print((reverse(a)))


if __name__ == "__main__":
   main()


