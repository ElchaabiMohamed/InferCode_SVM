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
   i = str[0]
   letter_pos = 1
   if letter in str:
      letter_pos = i + 1 
      return letter_pos 
   else:
      print("-1")
   
  