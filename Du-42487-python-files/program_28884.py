import time #for countdown

def countdown(num):
 i = 0
 while i < num:
  print(num - i)
  time.sleep(0.1)
  i = i + 1
 print("LIFT OFF!")

def search(str,letter):
 if letter in str:
  return "True"
 else:
  return "False" #won't work with print


