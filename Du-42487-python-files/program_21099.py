#Countdown
def countdown(num=3):
   while num!=0:
      print(num)
      num=num-1
   print("LIFT OFF!")
#Search
def search(ls,val):
   i= 0
   while i< len(ls):
      if ls[i] == val:
         return True
      i = i + 1
   return False
#Index
def index(ls,val):
   i= 0
   while i< len(ls):
      if ls[i] == val:
         return i
      i = i + 1
   return -1
#Fibonacci
def fibonacci(n):
   a=[0,1,1]
   i=3
   while i<n:
      a.append(a[i-1]+a[i-2])
      i=i+1 
   a.append(a[i-1]+a[i-2])
   return a[n]
