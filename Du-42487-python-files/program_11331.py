def countdown(num):
 import time
 while num != 0:
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
  position = 0
  if letter in str:
   position = position + 1
   return position
  else:
   return str + "-1"
