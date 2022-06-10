
def swap(a, i, p):
   tmp=a[i]
   a[i]=a[p]
   a[p]=tmp
   
def find_smallest(a, i):
   p=i
   j=i+1
   while j<len(a):
      if a[j]<a[p]:
         p=j
      j = j + 1
   return p

def selection_sort(a):
   i=0
   while i<len(a):
      p = find_smallest(a, i)
      swap (a, i, p)
      i+=1
   return a

def main():
   print(selection_sort([3, 5, 2, 9, 10, 3, 1]))

if __name__=="__main__":
   main()
      