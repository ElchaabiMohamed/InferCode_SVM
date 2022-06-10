#import sys
#a = sys.stdin.read().split()
#a = [int(x) for x in a]
#print a #4,2,1,3,5
#All of the above code is standard input from the command line, this is for lab sheet 12:3
def swapi(a,i,j):
   if a[j] < a[i]:
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      j = i
      while j < len(a):
         swapi(a,i,j)
         j += 1
      i += 1

if __name__ == "__main__":
   a = [1, 2, 3, 1, 2, 3]
   selection_sort(a)
   print(a)
