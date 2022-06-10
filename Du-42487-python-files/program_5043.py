# Swap the elements at positions i and j in list a.

def swap(a,i,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp
   
def reverse(a):
   a.reverse()
   
def main():
   print(swap(a,1,2))
   print(reverse(a))

if __name__=='__main__':
   main()   