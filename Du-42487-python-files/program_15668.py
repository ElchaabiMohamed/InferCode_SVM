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
   
