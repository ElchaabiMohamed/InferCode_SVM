#Countdown
def countdown(num=3):
   while num!=0:
      print(num)
      num=num-1
   print("LIFT OFF!")
#Search
def search(word, letter):
   if letter in word:
      print("True")
   else:
      print("False")
#Index
def index(word, letter):
   if letter not in word:
      print(-1)
   else:
      i=0
      while word[i]!=letter:
         i=i+1
      print(i)
#Fibonacci
def fibonacci(n):
   a=[0,1,1,2,3,5,8,13,21,34]
   if n<=1:
      print(a[n])
   elif n>1:
      print(a[n-1]+a[n-2])

#countdown(3)

#search("Hello", "h")

#index("hello","h")

#fibonacci(0)


