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
def index(word, letter):
   if letter not in word:
      return -1
   else:
      i=0
      while word[i]!=letter:
         i=i+1
      return i
#Fibonacci
def fibonacci(n):
   import math
   Phi=1.61803398875
   return int( ((Phi**n)-((1-Phi)**n))/math.sqrt(5) )

#countdown()

#search("Hello", "h")

#index("hello","h")

#fibonacci(0)


