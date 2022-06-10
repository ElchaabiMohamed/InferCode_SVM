def swap(a,i,p):
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   return a

def reverse(a):
   return a[::-1]

def main():
   a = [4, 3, 1, 2]
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):     
         if a[j] < a[p]:
            p = j
         j = j + 1
   
      print(swap(a,i,p))
      return


if __name__ == "__main__":
   main()























































































































































































