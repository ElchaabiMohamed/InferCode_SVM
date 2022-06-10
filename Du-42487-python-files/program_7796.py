import time
def countdown(num):
   while num > 0:
      print(num)
      time.sleep(0.1)
      num = num - 1
      if num == 0:
         print("LIFT OFF!")

def search(str,letter):
   if letter in str:
      return True
   else:
      return False

def index(str,letter):
   if letter in str:
      return str.find(letter)
   else:
      return -1

def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
