# Swap the elements at positions i and j in list a.

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   
def reverse(a):
   list(reversed(a))
   
def main():
   print(swap(a))
   print(reverse(a))

