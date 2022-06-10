#Countdown
def countdown(num=3):
   while num!=0:
      print(num)
      num=num-1
   print("LIFT OFF!")
#Search
def search(word, letter):
   if letter in word:
      return True
   else:
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
   return int( ((Phi**n)-((1-Phi)**n))/sqrt(5) )

#countdown(3)

#search("Hello", "h")

#index("hello","h")

#fibonacci(0)


