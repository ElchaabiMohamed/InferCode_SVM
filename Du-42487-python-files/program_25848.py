import time
import sys

def index(str,letter1,letter2):
   i = 0
   while i < len(str):
      if str[i] == letter1:
         return i
      i += 1
   return "-1"

   
def countdown(number):
   while int(number) > 0:
      print(number)
      number = number - 1
      time.sleep(0.1)
      
   print("LIFT OFF!")
   
   
def fibonacci(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fibonacci(n-1) + fibonacci(n-2)
	  

def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"



   i = 0
   while i < len(str):
      if str[i] == letter2:
         return i
      i += 1
   return "-1"


