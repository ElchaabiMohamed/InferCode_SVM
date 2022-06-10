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
   return n-1+n-2

#countdown(3)

#search("Hello", "h")

#index("hello","h")

#fibonacci(0)


