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
   a = [5, 4, 3, 2, 1]
   
   print((reverse(a)))


if __name__ == "__main__":
   main()


