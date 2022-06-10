import time

def countdown(num):
   while int(num) > 0:
      print(num)
      num = num - 1
      time.sleep(0.1)
      
   print("LIFT OFF!")


def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"


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
