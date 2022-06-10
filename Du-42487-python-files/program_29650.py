#
import time


def countdown(num):
   while num > 0:
      print(num)
      num = num - 1
      if num == 0:
         time.sleep(1.0)
         print("LIFT OFF!")
 
def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"
 

   