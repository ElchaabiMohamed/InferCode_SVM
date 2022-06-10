def swap(a,i,j):
   a[i], a[j] = a[j], a[i]
   return a

def reverse(a):
   i=0
   while i < len(a)/2:
      a[len(a)-i-1], a[i] = a[i], a[len(a)-i-1]
      i += 1
   return a
def main():
   
   print(swap(a, i, j))
   print(reverse(a))

if __name__ == "__main__":
   main()
