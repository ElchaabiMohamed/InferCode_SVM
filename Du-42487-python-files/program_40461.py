import sys

def swap(a,i,j):
  tmp = a[j]
  a[j] = a[i]
  a[i] = tmp
  
def reverse(a):
  return a.reverse()
  
def main():
  print(swap(a,2,3))
  print(reverse(a))
  
if __name__ == "__main__":
   main()