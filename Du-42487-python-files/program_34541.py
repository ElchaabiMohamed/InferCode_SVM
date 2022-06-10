import time
def countdown(num):
   i = 0
   while i < num:
      time.sleep(0.1)
      return int(num[i])
      i = i + 1
   return "LIFT OFF !"
