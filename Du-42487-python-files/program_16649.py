#!bin/usr/env python

def countdown(num):
   import time
   while num != 0:
      print(num)
      time.sleep(0.1)
      num = num-1
   print("LIFT OFF!")
   
   
def search(str, letter):
   for item in str:
      if item == letter:
         return True
   return False
   
def index(str, letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return i
      else:
         i = i+1  
   if i == len(str) and str[i] != letter:
      return -1