def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   return a

def reverse(a):
   for i in range(0, len(a) / 2):
      a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]



def main():
   a = [4, 3, 1, 2]
   print(swap(a,i,j))
   print(reverse(a))



if __name__ == "__main__":
   main()























































































































































































