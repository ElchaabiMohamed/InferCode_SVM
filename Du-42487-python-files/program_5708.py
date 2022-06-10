#Countdown
def countdown(num=3):
   if num!=0:
      print(num)
      countdown(num-1)
   else:
      print("LIFT OFF!")
#Search
def search(ls,val,na=0):
   pos=len(ls)
   if pos == len(ls):
      return False
   elif ls[pos] == val:
      return True
   else:
      return search(ls,val,pos+1)
#Index
def search(ls,val,pos):
   if pos == len(ls):
      return False
   elif ls[pos] == val:
      return True
   else:
      return search(ls,val,pos+1)
#Fibonacci
def fibonacci(n):
   a=[0,1,1]

   i=3
   while i<n:
      a.append(a[i-1]+a[i-2])
      i=i+1 
   a.append(a[i-1]+a[i-2])

   return a[n]



