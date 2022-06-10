import time

def countdown(num):
   i = 0
   while int(num) > 0:
      num = int(num) - i
      print(num)
      time.sleep(0.1)
      i += 1
   print("LIFT OFF!")
