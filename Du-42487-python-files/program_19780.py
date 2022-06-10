import time
import sys

def countdown(num):
   while num > 0:
      print(num)
      num = num - 1
      if num == 0:
         sys.stdout.write(num)
         time.sleep(1.0)
         print("LIFT OFF!")