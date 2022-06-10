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
 

def index(str,letter):
   pos_letter = 1 
   i = 0 
   while i < len(str):
      if letter in str:
         pos_letter = i + 1
         i = i + 1 
         return pos_letter
   else:
      return "-1"