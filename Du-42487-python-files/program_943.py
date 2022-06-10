a=[4,3,1,2]
b=[]
def swap(a,i,j):
   tmp=a[i]
   a[i]=a[j]
   a[j]=tmp
   return a  
def reverse(a):
   i=0
   while i<len(a):
      b.append(a[len(a)-1-i])  
      i=i+1 
   a=b
   return a
   
def main():
   print(swap(a,2,3))
   print(reverse(a))

if __name__ == "__main__":
   main()