import time

def countdown(num):
   while num >= 1:
      print(num)
      time.sleep(0.1)
      num = num - 1

   print("LIFT OFF!")

def search(str,letter):
   if letter in str:
      return "True"
   else:
      return "False"

def index(str,letter):
   if letter not in str:
      return "-1"
   i = 0
   while i < len(str):
      if letter == str[i]:
         return i
      i += 1

