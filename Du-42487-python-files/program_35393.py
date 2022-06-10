import time

def countdown(num):
 i = 0
 while i < num:
  print(num - 1)
  time.sleep(0.1)
  i = i + 1
 print("LIFT OFF!")

