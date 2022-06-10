import time

def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"

def countdown(number):
   while int(number) > 0:
      print(number)
      number = number - 1
      time.sleep(0.1)
      
   print("LIFT OFF!")

def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return i
      i += 1
   return "-1"


def fibonacci(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fibonacci(n-1) + fibonacci(n-2)