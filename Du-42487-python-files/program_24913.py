import time
def countdown(num):
   i = 0
   while i < len(num):
      time.sleep(0.1)
      return num[i]
      i = i + 1
   return "LIFT OFF !"
