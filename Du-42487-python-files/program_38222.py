import time

def countdown(num):
   while num >= 1:
      print(num)
      time.sleep(0.1)
      num = num - 1

   print("LIFT OFF!")

def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"

def index(str,letter):
   if letter not in str:
      return "-1"
   i = 0
   while i < len(str):
      if letter == str[i]:
         return i
      i += 1

def fibonacci(n):
   fib = [0,1,1,2,3,5,8,13,21,34]

   i = 10
   while i < 20:
      new = int(fib[(i-1)]) + int(fib[(i-2)])
      fib.append(new)
      i += 1
   
   j = 1
   while j < len(fib):
      if j == n:
         return fib[j]
      j += 1

   if n == 0:
      return 0