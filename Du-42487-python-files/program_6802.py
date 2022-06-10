
#!/usr/env python
import time
def countdown(num):
   while num >= 1:
      print(num)
      time.sleep(0.1)
      num -= 1
   print("LIFT OFF!")

def search(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return True
      i += 1
   return False

def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return i
      i += 1
   return -1

def fibonacci(n):
   if n == 0:
      return n
   elif n == 1:
      return n
   else:
      a = 0
      b = 1
      i = 2 
      while i <= n:
         sum1 = a + b
         a = b
         b = sum1
         i += 1
      return sum1
         
      
      
   
   
