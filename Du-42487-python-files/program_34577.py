import time

def countdown(num):
   while int(num) > 0:
      print(num)
      num = num - 1
      time.sleep(0.1)
      
   print("LIFT OFF!")


def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"


def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return i
      i += 1
   print("-1")
