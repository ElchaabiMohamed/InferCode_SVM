a=["apple","orange","pear"]

def swap(a,i,j):
   tmp=a[i]
   a[i]=a[j]
   a[j]=tmp
   return a  
def reverse(a):
   b=[]
   i=0
   while i<len(a):
      b.append(a[len(a)-1-i])  
      i=i+1 
   return b
   
def main():
   print(swap(a,0,1))
   print(reverse(a))

if __name__ == "__main__":
   main()