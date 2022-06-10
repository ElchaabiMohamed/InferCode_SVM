#
import time


def countdown(num):
   while num > 0:
      return num
      num = num - 1
      if num == 0:
         time.sleep(1.0)
         return "LIFT OFF!"
 
def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"
 

   