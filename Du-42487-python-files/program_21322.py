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
         return len[:i]
      i += 1
   return -1
   
     



      
   
  
