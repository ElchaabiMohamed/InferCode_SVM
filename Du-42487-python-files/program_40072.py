

def swap(a, i, j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp    
    return a

def reverse(a):
   i = 0
   while i < len(a)/2:
      swap(a,i,len(a)-1-i)
      i = i + 1   
   
   #return a[::-1]

# Your function goes here.

def main():
   a = [4,3,1,2]
   swap(a, 0, 3)
   print(a)


   b = [1,2,3,4,5]
   reverse(b)
   print(b)

if __name__ == "__main__":
   main()



