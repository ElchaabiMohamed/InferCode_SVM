import time

def countdown(num):
   while num >= 1:
      print(num)
      time.sleep(0.1)
      num -= 1
   print("LIFT OFF!")
   return num

def search(str,letter):
   if letter in str:
      return True
   else:
      return False
   

def index(str,letter):
   i = 0
   while i < len(str) and str[i] != letter:
      i += 1
   if letter in str:
      return i
   else:
      return '-1'

def fibonacci(n):
   if n ==0:
      return '0'
   elif n == 1:
      return '1'
   else:
      n1 = 1
      n2 = 0
      
      i = 2
      while i <= n:
         sum1 = n1 + n2
         n2 = n1
         n1 = sum1
         i += 1
      return sum1
      
