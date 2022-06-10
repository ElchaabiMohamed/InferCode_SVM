#!/usr/bin/env python
import time


def countdown(num):
   while num >= 1:
      print(num)
      num -= num
      time.sleep(0.1)
   print("LIFT OFF!")

def search(str,letter):
   for item in str:
      if item == letter:
         return True
   return False
 
def index(str,letter):
   i = 0
   if letter in str:
      x = letter[0]
      for ch in str:
         if ch == x:
            if str[i:i+len(letter)] == letter:
               return i
         i += 1
   return - 1
 
def fibonacci(n):
   if n == 0: 
      return 0
   elif n == 1: 
      return 1
   else: 
      return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
   print('calling countdown("10")')
   countdown(10)
   print("LIFT OFF!")
 
if __name__ == '__main__':
   print('calling search("python","a")')
   search('python','a')
   print('calling search("python","h")')
   search('python','h')
 
if __name__ == '__main__':
   print('calling index("python","a")')
   index("python","a")
   print('calling index("python","h")')
   index("python","h")
 
 
   
      
