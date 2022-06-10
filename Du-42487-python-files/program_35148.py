import time

def countdown(number):
   while number > 0:
      print(number)
      time.sleep(.1)
      number -= 1
      if number == 0:
         print("LIFT OFF!")

def search(str,letter):
   i = 0
   while i < len(str):
      if letter in str:
         return True
      else:
         return False
      i += 1

def index(str,letter):
   if letter not in str:
      return -1
   else:
      return str.find(letter)
	  
def fibonacci(n):
   if n < 2:
      return n
   return fibonacci(n-2) + fibonacci(n-1)