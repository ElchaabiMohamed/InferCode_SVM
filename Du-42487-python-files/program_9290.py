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
   import math
   Phi=1.61803398875
   return int( ((Phi**n)-((1-Phi)**n))/math.sqrt(5) )

#countdown()

#search("Hello", "h")

#index("hello","h")

#fibonacci(0)


